### 手机抓包的环境

mac + iOS + charles

### 抓包的原理

手机通过代理的形式 找 电脑 找 charles 找 百度

###  http和https

- http 
  - 设置代理即可
- https
  - ssl证书

### 总结

- 电脑的操作
  - proxy - proxy setting - http proxy 打钩 端口号：8888
  - proxy - ssl proxy setting - enable ssl proxying 打钩 下方填写需要查看的地址，如果都需要输入*，端口是443
  - help - ssl proxying 安装root证书 （第二组，第一个）证书选择始终信任
  - help - ssl proxying 在远程设备安装root证书 （第二组，第四个）
- iOS手机的操作
  - 在手机中，打开chls.pro/ssl安装描述文件
  - 在 设置 - 通用 - 描述文件与设备管理 会多一个证书。
  - 在 设置 - 通用 - 关于手机 最下方 - 证书信任设置 打开对 charles proxy 证书的信任
- android手机的操作
  - 在手机中，打开chls.pro/ssl安装描述文件
  - 起名，确定
