# Order Strange Api


## 安装环境

> Todo...

## 安装步骤

#### 一、克隆代码

```
git clone https://github.com/yellowLinw/OrderStrange-Api.git
```

#### 二、安装依赖

```
pip install -r requirements.txt
```

#### 三、修改配置

复制环境配置文件

```bash
cp .env.example .env
```

#### 四、数据库迁移

```
flask db init
flask db migrate  #修改迁移,插入初始数据
flask db upgrade
```

#### 五、配置服务器
> Todo...

#### 六、部分命令

```
生成引用库requirements
pipreqs [options] <path> --encoding=utf8 --force
    
生成安装类库requirements
pip freeze
```

