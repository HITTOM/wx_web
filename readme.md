# 使用说明

## 启动与交互
### 启动
python main.py 80
### 网页访问调试
访问 http://81.70.157.252/wx 会调用GET接口
![image](https://user-images.githubusercontent.com/24716146/164978057-b878546b-37c6-49d0-b2bd-ae0a7f4d59c1.png)
### 公众号请求
用户向公众号请求消息 会调用POST接口
![image](https://user-images.githubusercontent.com/24716146/164978682-c05a8c76-d336-4070-9ce5-fa4f8b6ad06b.png)

（回包数据要用xml格式，暂没来得及封装，因而会报错）
## 公众号绑定
接入[微信开发者中心](https://mp.weixin.qq.com/)绑定url即可
![image](https://user-images.githubusercontent.com/24716146/164978142-bdbfd184-292a-488e-9a3f-8c96df8ac985.png)
