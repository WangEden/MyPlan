1.制作Windows启动盘
2.启动Windows启动盘后点击疑难杂症 —> 命令提示符
3.依次输入

```bat
bootrec /fixboot
bootrec /fixmbr
bootrec /rebuildbcd
```

如果出现拒绝访问，则输入

```bat
bootsect /nt60 sys
```

输入后即可继续上面的命令

4.返回疑难杂症页面，修复Windows，这时候这个启动盘的Windows已经能找到之前安装的Windows系统了