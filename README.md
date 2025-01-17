# IntelligentAlgorithm-CloudScheduler

#### 介绍
用智能算法解决云计算调度类问题，可以更换评价函数、绘图并存储结果和图表
需要注意的是，全都是离散调度问题，也就是说所有粒子群都是离散粒子群算法

#### 代码结构

- simulate.py: 运行得到结果，可以在其中更换算法、数据、参数等
- SchedulerScaleandFitness.py: 多个算法对比最优解以及收敛曲线
- Schedulers.py: 同上，不同组别对比实验
- chaosTest.py: 同上，不同组别对比实验

utils.Entities 定义实体:
- Cloudlet: 云任务 cloud tasks to allocated
- VM: 虚拟机 Virtual Machines to execute tasks(cloudlets)

schedulers/*.py 用来仿真的预定义算法  , Support Algorithms.
并非每一个算法都有论文依据，因为这些算法里面有自己的改进尝试。
- GA: Genetic Algorithm 遗传算法
- SA: Simulated Annealing Algorithm 模拟退火算法
- ACO: Ant Colony Optimization Algorithm 蚁群算法
- PSO: Particle Swarm Optimization Algorithm 粒子群算法
- CRPSO: Chaotic Hierarchical Gene Replication 基于混沌策略的基因层次复制优化算法
- DPSO: discrete PSO离散粒子群算法
- CDPSO: Chaotic PSO 基于混沌优化策略的离散粒子群算法
- TSA: Taboo Search Algorithm 禁忌搜索算法
- others

ChaosDPSO（混沌优化离散粒子群算法）、ChaosHPSO（稍作修改的混沌优化粒子群算法）、newPSO（稍作改进提升粒子群算法）、DPSO（二进制粒子群算法，不过其实是普通的离散粒子群算法）、ACO（蚁群算法）、SA（模拟退火算法）、GA（遗传算法）、TS（禁忌搜索算法有待修改，目前可能有误）

utils/*.py: 工具类

其他以及为介绍的代码都是工具类或者当年的废弃代码

#### 安装教程

1.  不需要安装
2.  下载下来直接在Scheduler.py使用即可


#### 使用说明

1.  实验对象参数有改动，在Entities.py里面修改，例如添加实验属性
2.  其他算法如需改动流程，在对应算法里面修改
3.  在Scheduler.py里直接修改各个算法的种群数量和迭代次数，也可统一修改
4.  是否生成数据或生成图片并保存到本地，通过在Scheduler.py注释相应代码修改
5.  粒子群的改进在于产生新解时用了一些倒置、交换、移动等等操作增强产生新解的能力

#### Reference

1. Holland J.(1992). [Genetic Algorithm](https://doi.org/10.1038/scientificamerican0792-66)
2. Kennedy J, Eberhart R.(1995). Particle Swarm Optimization 
3. Ke Zhao.(2021). [Research on Edge Cloud Load Balancing Strategy based on Chaotic Hierarchical Gene Replication](https://www.fujipress.jp/jaciii/jc/jacii002600050758/)

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码，注意必须统一代码风格
4.  新建 Pull Request

