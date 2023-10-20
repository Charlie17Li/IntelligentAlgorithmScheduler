#!/usr/bin/env python

import time
import random
import json

from kubernetes import client, config, watch
from sdcclient import SdcClient

config.load_incluster_config()
k8s_client = client.CoreV1Api()
sdclient = SdcClient(open("/etc/sysdigtoken/token.txt","r").read().rstrip())
sysdig_metric = "net.http.request.time"
metrics = [{ "id": sysdig_metric, "aggregations": { "time": "timeAvg", "group": "avg" } }]

scheduler_name = "sysdigsched"


def get_request_time(hostname):
    hostfilter = "host.hostName = '%s'" % hostname
    start = -60
    end = 0
    sampling = 60
    metricdata = sdclient.get_data(metrics, start, end, sampling, filter=hostfilter)
    request_time = float(metricdata[1].get('data')[0].get('d')[0])
    print hostname + " (" + sysdig_metric + "): " + str(request_time)
    return request_time


def best_request_time(nodes):
    if not nodes:
        return []
    node_times = [get_request_time(hostname) for hostname in nodes]
    best_node = nodes[node_times.index(min(node_times))]
    print "Best node: " + best_node
    return best_node


def nodes_available():
    ready_nodes = []
    for n in k8s_client.list_node().items:
            for status in n.status.conditions:
                if status.status == "True" and status.type == "Ready":
                    ready_nodes.append(n.metadata.name)
    return ready_nodes


def scheduler(name, node, namespace="default"):
    body=client.V1Binding()
    target=client.V1ObjectReference()
    target.kind="Node"
    target.apiVersion="v1"
    target.name= node
    meta=client.V1ObjectMeta()
    meta.name=name
    body.target=target
    body.metadata=meta
    return k8s_client.create_namespaced_binding(namespace, body)


def main():
    w = watch.Watch()
    for event in w.stream(k8s_client.list_namespaced_pod, "default"):
        if event['object'].status.phase == "Pending" and event['object'].spec.scheduler_name == scheduler_name:
            try:
                print "Scheduling " + event['object'].metadata.name
                res = scheduler(event['object'].metadata.name, best_request_time(nodes_available()))
            except client.rest.ApiException as e:
                print json.loads(e.body)['message']


if __name__ == '__main__':
    main()                                                                                                                                                                  76,1