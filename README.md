基于face_recognition的人脸识别demo
==========
## 功能
    1、提供姓名和照片进行人脸照片与姓名信息的初始化
    2、提供姓名和待匹配照片，进行人脸识别比对，返回人脸匹配结果
        
## 依赖
    1、cmake
    2、dlib
    3、python2.7
    4、Flask
    5、mongodb
    6、gunicorn
    7、face_recognition

## 安装
#### 准备环境
    1、安装python2.7
    2、安装mongodb
    3、安装pip
    4、安装cmake（建议3.x以上）
    5、安装dlib，安装步骤参见
        https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf
        若遇到问题，可参见https://rhodian.iteye.com/admin/blogs/2439706，希望可以解决问题
    6、使用pip安装face_recognition
    7、使用pip安装Flask、gunicorn（启动时如果还有依赖问题，请按依赖提示安装依赖模块）
        
#### 配置文件
    cd <项目路径>
    vim config.py
        
#### 启动
    启动方式依赖gunicorn，请确保已经安装依赖模块。
    启动命令建议：gunicorn -b 0.0.0.0:5000 -D run:app
        
#### 访问
    1、照片初始化：http://127.0.0.1:5000/upload_faceimg_to_init
        参数：name、file
        返回：初始化成功
    2、人脸比对http://127.0.0.1:5000/upload_faceimg_to_recognition
        参数：name、file
        返回：确认过眼神，是同一个人  或者   人脸匹配失败
        
#### 其他