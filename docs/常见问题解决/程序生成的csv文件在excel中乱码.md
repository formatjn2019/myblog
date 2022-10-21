程序生成的csv文件在excel中乱码

在某些程序的制作过程中，有可能需要读取或者写入csv文件，它能用excel以表格形式打开，同时以文本形式以记事本打开。使用程序生成时也不必依赖三方类库。可以说是一种比较方便的文件交换形式。

但是有时候程序写入的csv文件会在记事本中打开正常，而excel中打开乱码。

如果程序写入的是utf8编码，那么就是头的问题，即excel默认读取的是utf8bom

这时候有两种解决办法

#### 1. 更改写入格式为gbk

这样能避免utf8bom的问题，统一为程序读写读写编码为gbk(gb2312)

#### 2. 手动写入bom

以go语言为例

在其它写入操作前，先在文件中写入头

即`\xEF\xBB\xBF` 三个字节的数据

或者写入`\uFEFF`

```go
file, _ := os.OpenFile(filePath, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 438)
defer file.Close()
//excel 乱码问题，插入头
file.WriteString("\xEF\xBB\xBF")
//file.WriteString("\uFEFF")
```

在读取文件时，忽略写入的三个字节

```go
file, _ := os.OpenFile(filePath, os.O_RDONLY, 438)
defer file.Close()
file.Seek(3, 0)
```
