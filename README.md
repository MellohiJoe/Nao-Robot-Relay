# NAO Robot Relay
NAO机器人接力

## 设计文档

### 目录结构

- **Bot1** _先出发的机器人的相关代码_
  - **Entity**
    - RedBallData.py
  - **Mod**
    - RedBallMod.py 红球识别数据控制器(属于视觉任务)
  - **Task**
    - Caller.py 通知另一个机器人
    - Sensor.py 超声任务
    - Talker.py 声音任务
    - Viewer.py 视觉任务
    - Walker.py 行动任务
  - modules.py 全局创建的naoqi代理模块
  - BotEvents.py 所有任务的接口
  - start.py 启动机器人、执行任务 
- **Bot2**

### 开发方案

请在具体的任务实现后，将代码移植到 **Task** 目录下某一个类中； 

> 这些类有 Walker, Viewer, Sensor, Caller ...

它们都继承 **BotEvents** 这一接口，将部分实现其中的功能；

_请查阅接口定义的注释，以实现具体的函数_

### 实体(Entity目录下)

- **RedBallData**
  - **is_wrong**
    - bool
    - 是否存在红球&有效识别
  - **centerX**
    - float
    - 红球的横向偏角，单位：弧度，取值范围：-Pi/2 ~ Pi/2
    - 例如`-0.4`时红球偏向机器人右侧的前方，`0.4`时在左侧的前方，`+-0.04`时大致位于正前方

### 接口(BotEvents)

_注：time 规定了方法允许阻塞，或最长允许的执行时间_

1. **init_move 姿态初始**
   - desc: 到预备姿态
   - time: 阻塞
   - return: 无

2. **sensor_to_start 启动前的超声检测**
   - desc: 检测开始信号（超声波），若没有一直等
   - time: 循环+阻塞
   - return: 无

3. **sound_to_start 启动前的声音检测**
   - desc: 检测开始信号（声音），若没有一直等
   - time: 循环+阻塞
   - return: 无

4. **vision_to_start 启动前的视觉检测**
   - desc: 检测开始信号（视觉），若没有一直等
   - time: 循环+阻塞
   - return: 无

5. **on_enter_loop 事件回调接口**
   - desc: 进入主循环事件回调接口
     - 例如以下：
       - 开始视觉
       - 开始超声波
     - 由任务各自实现，主流程中调用
   - time: 瞬间，不阻塞
   - return: 无

6. **on_exit_loop 事件回调接口**
   - desc: 退出主循环事件回调接口
     - 例如以下：
       - 结束视觉
       - 结束超声波 
   - time: 瞬间，不阻塞
   - return: 无

7. **start_move 启动开始移动**
   - desc: 从静止开始前进
   - time: 瞬间，不阻塞
   - return: 无

8. **pose_vision 移动过程中视觉检测出的偏移**
    - desc: 视觉检测出Nao运动的偏移角度
    - time: 无阻塞
    - :return: RedBallData(详见实体类)

9. **adjust_move 得到偏移量后进行调整**
   - desc: 根据当前机器人的位姿，调整移动方向
   - param data: 由**pose_vision**返回的
   - time: 瞬间，不阻塞
   - return:无 

10. **detect_to_arrive 是否到达终点**
    - desc: 判定是否达到终点
    - time: 不阻塞
    - return: Boolean

11. **call_friend 通知另一个机器人**
    - desc: TCP通知另一个机器人
    - time: 无阻塞
    - return: Boolean

12. **stop_move 停止移动**
    - desc: 停止移动
    - time: 无阻塞
    - return: 无
