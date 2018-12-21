# rasa_test_ch
---

基于rasa的多轮问答学习和测试

rasa core 对话管理

rasa nlu 语义理解：意图识别和实体识别


## 安装相关组件包

```bash
pip install rasa_nlu==0.13.4
pip install rasa_core==0.11.4
pip install rasa_core_sdk==0.11.4
```


## 安装语料训练工具

```bash
yum install npm
npm install -g chatito
```

图像化的语料生成工具：npm i -g rasa-nlu-trainer


## 准备语料数据，编写需要的格式的语料数据。

rasa_core部分：

stories.md ：编写对话场景流程 	（-s）

domain.md ：意图，动作，反馈以及实体和槽，机器知识库。	（-d）

rasa_nlu部分：

nlu_config.yml ：nlu模型算法处理流程 （-c）

data.json ：训练数据	（--data）


## 训练词向量模型，训练rasa_core模型，训练自己的rasa_nlu模型。

训练rasa_nlu：python -m rasa_nlu.train -c my_config.yml --data data/bank.json --path models

训练rasa_core:  python -m rasa_core.train -d data/bank_domain.yml -s data/bank_story.md -o models/dialogue

运行：python -m rasa_core.run -d models/dialogue -u models/default/model_20181219-155903/

单独运行core：python -m rasa_core.run -d models/dialogue

测试：

```bash
/greet
/ask_money{"money": "人民币"}
```

单独运行nlu：// 启动服务

```bash
python -m rasa_nlu.server -c my_config.yml --path models
```

//测试服务：

```bash
curl -XPOST localhost:5000/parse -d '{"q":我想去柜台取人民币？", "project": "", "model": "model_20180912-202427"}' | python -mjson.tool
```

## 语料(data.json )标注平台：

[chattio](https://github.com/rodrigopivi/Chatito)用来应对没有数据冷启动时的训练数据，如果有数据建议使用rasa-nlu-trainerr平台标注。

```bash
rasa-nlu-trainer -p 10000 --source data/bank.json
```

## domain.md 编写：

 标识    |    说明
----------------- | -----------------
 intents | 意图
 entities | 实体
 slots | 槽
 templates | 回答模板
 actions | 动作

## stories.md 编写：

符号    |    说明
----------------- | -----------------
 ##| story标题
 *| 意图
 -| 动作

## 自定义 action 添加 ：

事先需要安装 rasa_core_sdk

action分为3大类：

1.default action：（action_listen，action_restart，action_default_fallback）

2.utter action：以utter_开头的action，用于给用户发送信息。

3.custom action：用户自定义的action

action服务的配置endpoints.yml:

```yml
action_endpoint:
  url: "http://localhost:5055/webhook"
```

在core的运行命令之后加上：--endpoints endpoints.yml

```bash
python -m rasa_core.run -d models/dialogue/ -u models/default/model_20181220-110910/ --endpoints endpoints.yml
```

同时如果你自定义的action文件名叫actions.py，那么，你需要事先运行如下命令启动你的action：

```bash
python -m rasa_core_sdk.endpoint --actions actions
```

action_default_fallback 可用于回滚操作 具体参看fallback actions
