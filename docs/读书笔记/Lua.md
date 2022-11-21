# Lua

## 环境搭建

### 源码下载

- lua官网

### 编译源码

- win

	- 使用教程

		- 图

	- 编译脚本

		- @echo off
:: ========================
:: build.bat
::
:: build lua to dist folder
:: tested with lua-5.3.5
:: based on:
:: https://medium.com/@CassiusBenard/lua-basics-windows-7-installation-and-running-lua-files-from-the-command-line-e8196e988d71
:: ========================
setlocal
:: you may change the following variable’s value
:: to suit the downloaded version
set work_dir=%~dp0
:: Removes trailing backslash
:: to enhance readability in the following steps
set work_dir=%work_dir:~0,-1%
set lua_install_dir=%work_dir%\dist
set compiler_bin_dir=%work_dir%\tdm-gcc\bin
set lua_build_dir=%work_dir%
set path=%compiler_bin_dir%;%path%
cd /D %lua_build_dir%
make PLAT=mingw
echo.
echo **** COMPILATION TERMINATED ****
echo.
echo **** BUILDING BINARY DISTRIBUTION ****
echo.
:: create a clean “binary” installation
mkdir %lua_install_dir%
mkdir %lua_install_dir%\doc
mkdir %lua_install_dir%\bin
mkdir %lua_install_dir%\include
mkdir %lua_install_dir%\lib
copy %lua_build_dir%\doc\*.* %lua_install_dir%\doc\*.*
copy %lua_build_dir%\src\*.exe %lua_install_dir%\bin\*.*
copy %lua_build_dir%\src\*.dll %lua_install_dir%\bin\*.*
copy %lua_build_dir%\src\luaconf.h %lua_install_dir%\include\*.*
copy %lua_build_dir%\src\lua.h %lua_install_dir%\include\*.*
copy %lua_build_dir%\src\lualib.h %lua_install_dir%\include\*.*
copy %lua_build_dir%\src\lauxlib.h %lua_install_dir%\include\*.*
copy %lua_build_dir%\src\lua.hpp %lua_install_dir%\include\*.*
copy %lua_build_dir%\src\liblua.a %lua_install_dir%\lib\liblua.a
echo.
echo **** BINARY DISTRIBUTION BUILT ****
echo.
%lua_install_dir%\bin\lua.exe -e "print [[Hello!]];print[[Simple Lua test successful!!!]]"
echo.

:: configure environment variable
:: https://stackoverflow.com/a/21606502/4394850
:: http://lua-users.org/wiki/LuaRocksConfig
:: SETX - Set an environment variable permanently.
:: /m Set the variable in the system environment HKLM.
setx LUA "%lua_install_dir%\bin\lua.exe" /m
setx LUA_BINDIR "%lua_install_dir%\bin" /m
setx LUA_INCDIR "%lua_install_dir%\include" /m
setx LUA_LIBDIR "%lua_install_dir%\lib" /m

pause
————————————————
版权声明：本文为CSDN博主「CoderHustlion」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/techfield/article/details/82883299

	- 编译器

- linux

### 运行方式

- 执行

	- 直接执行

		- lua 文件名

	- 执行后进入交互模式

		- lua -i prog

	- 交互模式下调用

		- dofile("prog.lua")

- 独立解释器

	- 第一行以井号开头，那么解释器在加载文件时会忽略这一行。
	- lua命令

		- lua [options] [ script [args] ]
		- 参数

			- -e

				- 直接在命令行中输入代码

			- -l

				- 用于加载库

## 数据类型

### nil ( 空 )

- 代表无效值

### boolean ( 布尔 )

- 有true和false两个值
- 逻辑运算符为 and or not

	- and

		- 如果第一个操作数为false则返回第一个操作数，否则返回第二个操作数

	- or

		- 第一个操作数不为false则返回第一个操作数，否则返回第二个操作数

	- a and b or c

		- 等价于三目运算符
		- b的值不为假，否则永远结果为c

	- and 的优先级高于 or
	- 都是短路求值

- 判断时将false和nil当做假，其余为真

### number ( 数值 ) 

- 5.3以后分为64位的integer类型和64位的float类型
- float支持2^53的整数类型，一般不会出现兼容问题
- 表示支持科学计数法
- 还支持以0x开头的16进制浮点数
- 除非两个运算数字都是整数（除法除外），否则结果为浮点数
- 取模

	- 定义

		- a % b == a - ((a // b) * b)
		- 可对浮点数取模

- 数学库

	- 三角函数

		- sin cos tan asin 等
		- 以弧度为单位
		- 可以用deg和rad进行角度和弧度的转换

	- 指数函数
	- 取整函数

		- floor

			- 向负无穷取整

		- ceil

			- 向正无穷取整

		- modf

			- 向0取整

		- 常用的四舍五入可以用 floor（数字+0.5）

			- 大数字容易出错

		- 转整数

			- 通过与0进行按位与计算可以将浮点数转为整数
			- math.tointeger()

	- 最大最小函数
	- 伪随机数函数
	- 常量pi和huge

- 表示范围

### string （ 字符串 )

- 不可变值
- 可使用长度操作符（#）获取字符串的长度
- 可以使用连接字符串..来进行字符串连接
- 可以使用单引号或双引号声明字符串
- 字符串标准库

	- string.len(s)

		- 字符串长度

	- string.rep(s,n)

		- 字符串重复n次

	- string.reverse

		- 字符串翻转

	- string.lower(s)

		- 转换成小写字母

	- string.upper(s)

		- 转换成大写字母

	- string.sub(s,i,j)

		- 从字符串中提取从i到j个字符
		- 包括i和j

	- string.char()

		- int转字符

	- string.byte()

		- 字符转int

	- string.format()

		- 代码格式化

	- string.find(origin,match)

		- 返回匹配的字符的开始和结束位置

- lua中的大多数函数使用字节索引

	- utf8.offset()函数可以将字符位置换为字节位置

### userdata ( 用户数据 )

### function  ( 函数 )

- 调用函数时使用的参数个数可以与使用的参数个数不一致。Lua语言会通过抛弃多余参数和将不足的参数设为nil的方式来调整参数的个数。
- 多返回值

	- 表构造器会完整地接收函数调用的所有返回值，而不会调整返回值的个数
	- return语句是不需要加括号的，当加括号时，返回值的个数只有一个

- 可变参数

	- 在参数列表中用 ... 表示

- table函数

	- table.unpack

		- 将列表拆分

- Lua支持尾调用消除

### thread ( 线程 )

### table ( 表 )

- 表是Lua中最主要（事实上也是唯一的）和强大的数据结构。
- Lua语言中表的本质是一种辅助数组（associate array），这种数组不仅可以使用数值作为索引，也可以使用字符串或其他任意类型的值作为索引（nil除外）。
- 表永远是匿名的，表本身和保存表的变量之间没有固定的关系
- 创建表

	- a={}
	- 构造器中的逗号可以使用分号代替

- 索引

	- a = {x = 10 , y = 20} 等价于 a = {}; a.x =10; a.y = 20
	- a.x等价于a["x"]
	- a[x]

- 使用长度操作字符串操作表

	- print(a[#a])

		- 输出序列‘a’的最后一个值

	- a[#a] = nil

		- 移除最后一个值

	- a[#a + 1] =v

		- 把‘v’加到序列的最后

- 遍历

	- 遍历所有键（无序）

		- for k,v in pairs(t) do

	- 遍历列表（有序）

		- for k,v in ipairs(t) do
		- 索引遍历 for k = 1, #t do

- 安全访问

	- 判断库中是否存在某个函数

		- 将复杂的判断替换
		- (((company or {}).director or {}).address or {}) .zipcode

			- 或者将{}替换为变量

- 修改

	- 插入

		- table.insert(t,index,value)

			- 不加index将插入到最后

	- 移动

		- table.move(a, f, e, t)

			- 将表a中索引f到e的元素移动到位置t上

		- table.move(a,1,#a,1,{})

			- 将所有元素进行拷贝

- 数据结构的实现

	- 数组

		- 可以通过表构造器在一句表达式中同时创建和初始化数组

			- square = {1, 4, 9 , 16}

		- 利用数据描述文件创建包含几百万个元素组成的构造器很常见

	- 多维数组
	- 队列
	- 反向表

		- 将键值互换

	- 字符串缓冲区

		- 为避免大字符串重复连接的问题，可以将表作为字符串缓冲区，然后使用table,concat返回字符串连接后的结果

## 环境

### 如果要测试一个变量是否存在，并不能简单地将它与nil比较。因为如果它为nil，那么访问就会引发一个错误。

- 应该使用rawget来绕过元方法

### 通常，_G和_ENV指向的是同一个表。但是尽管如此，它们是很不一样的实体。

- _ENV用于指向的是当前的环境
- _G在无人更改的其值的前提下，_G通常指向的是全局变量

## 语法

### 注释

- 单行

	- --

- 多行

	- --[[多行注释内容]]--

- 技巧

	- 注释代码时，用多行注释将其包裹，重新启用时，在第一行行首添加一个连字符即可

### 变量

- _ + 大写字母

	- 通常被用作特殊用途

- _ + 小写字母

	- 用作哑变量

### 分隔符

- 可用分号，也可以不写

### 全局变量

- 未初始化和被赋值nil的变量都是nil

### 局部变量和代码块

- 当需要更好地控制某些局部变量的生效范围时，do程序块也同样有用
- 局部变量可以避免由于不必要的命名而造成全局变量的混乱
- 局部变量还能避免同一程序中不同代码部分的命名冲突
- 访问局部变量比访问全局变量更快

	- local foo = foo
	- 用于提升foo的访问速度

- 局部变量会随着其作用域的结束而消失，从而使得垃圾收集器能够将其释放

### 判断类型

- type ( 变量 )

	- 返回一个字符串

### 控制结构

- if

	- if 条件 then
    语句 
elseif 条件 then
    语句
else
   语句
end

- while

	- while 条件 do
    语句
end

- repeat

	- repeat
   语句
until 条件

- for

	- 数值型

		- for var = exp1, exp2, exp3 do
   something
end
		- 三个参数为开始，结束， 步长，第三个参数可选

	- 泛型

		- for k, v in pairs(table) do
  something
end
		- for index,v in ipairs(table) do
  something
end
		- 可以用闭包自定义迭代器

- goto

	- 标签为::name::
	- 限制

		- 不能直接跳转到一个代码块中的标签
		- goto不能跳转到函数外
		- goto不能跳转到局部变量的作用域

## 编译、执行和错误

### 事实上函数dofile是一个辅助函数，函数dofile才完成了真正的核心工作

### loadfile

- loadfile是从文件中加载Lua代码，但它不会运行代码，而只是编译代码，然后将编译后的代码段作为一个函数返回。
- 与函数dofile不同，函数loadfile只返回错误码而不抛出异常。
- 相对于loadfile dofile更灵活，如果需要多次运行同一个文件

### load

- 与loadfile类似，不同之处在于该函数从一个字符串或函数中读取代码段，而不是从文件中读取
- load的函数操纵的是全局变量

## 迭代器和闭包

### 闭包

- 在Lua语言中，函数是严格遵循词法定界（lexical scoping）的第一类值(first-class value)
- 第一类值

	- 意味着Lua语言中的函数与其他常见的值具有同等权限：一个程序可以将某个函数保存到变量中（全局变量和局部变量均可）或表中，也可以将某个函数作为其他函数的返回值返回

- 词法定界

	- 意味着Lua语言中的函数可以访问包含其自身外函数中的变量（也意味着Lua语言完全支持Lambda演算）

- 函数没有名字，一般为全局变量存储
- 可用表将函数存储在局部变量中，为局部函数

	- Lib = {}
Lib.foo = function (x, y) return x +y end
	- Lib = {
    foo = function (x, y) return x + y end
}
	- Lib = {}
function Lib.foo (x,y) return x + y end

- 局部函数 

	- 函数体前加 local

### 泛型for

- 泛型for在循环过程中在其内部保存了迭代函数。实际上，泛型for保存了三个值：一个迭代函数、一个不可变状态（invariant state）和一个控制变量（control variable）

### 无状态迭代器（stateless iterator）

- 就是一种自身不保存任何状态的迭代器。因此，可以在多个循环中使用同一个无状态迭代器，从而避免创建新闭包的开销

## 元表和原方法

### 元表

- 对应方法

	- 乘法（*）

		- __mul

	- 加法（+）

		- __add

	- 减法（-）

		- __sub

	- 除法（/）

		- __div

	- floor除法（//）

		- __idiv

	- 负数（-）

		- __munm

	- 取模（%）

		- __mod

	- 幂运算（^）

		- __pow

	- 按位与（&）

		- __band

	- 按位或（|）

		- __bor

	- 按位异或（~）

		- __boxor

	- 按位取反（~）

		- __bnot

	- 向左移位（<<）

		- __shl

	- 向右移位（>>）

		- __shr

	- 连接运算符（...）

		- __concat

	- 等于（==）

		- __eq

	- 小于（<）

		- __lt

	- 小于等于（<=）

		- __le

	- 字符串生成

		- __tostring

	- pairs函数（lua 5.2）

		- __pairs

	- 设置元表（设置时防止他人更改元表）

		- __setmetatable

	- 获取元表（设置时防止他人获取元表）

		- __getmetatable

	- 空元素访问操作

		- __index

	- 空元素更新操作

		- __newindex

- 元表可以修改一个值在面对一个未知操作时的行为。
- 在两个表进行运算时，它会检查两者之一是否有元表（metatable）
- 在lua语言中，我们只能为表设置元表；如果要为其他类型的值设置元表，则必须通过c代码或调试库完成（改限制存在的主要原因是为了防止过度使用对某种类型的所有值生效的元表。）
- lua语言中的每一个值都可以有元表。每一个表和用户数据类型都具有各自独立的元表。而其他类型的值则共享对应类型所属的同一个元表。
- 可以使用setmetatable来设置或修改任意表的元表。
- 访问表中不存在的元素会得到nil。实际上，这些访问会引发解释器查找一个名为__index的元方法，如果没有这个元方法，那么就像一般情况下一页，结果就是nil；否则，则由这个元方法来提供最终结果。
- 如果我们希望在访问一个表时不调用__index元方法，那么可以使用函数rawget。
- 使用__index时，__index不仅可以是一个函数，还可以是一个表

	- 当__index是一个函数时，lua会使用表和表中不存在的值进行函数调用
	- 当__index是一个表时，会直接搜索这个表

- 代理的实现

	- 设置一个空的表
	- 具有用于跟踪所有访问并将访问重定向到原来的表的合理元方法

## 协程

### 状态

- 挂起（suspended）
- 运行（running）
- 正常（normal）
- 死亡（dead）

### coroutine

- yeild

	- 返回值为对应的resume的参数

- crate

	- 创建协程
	- 返回协程

- wrap

	- 创建协程
	- 返回函数
	- 不同于原始函数resume，函数的第一个值不是返回错误代码，而是遇到错误抛出异常

### Lua语言提供的是非对称的协程

- 需要两个函数控制协程的执行，一个用于挂起协程的执行，一个用于恢复协程的执行
- 一些人将非对称协程称为semi-coroutines
- 其他人使用相同的术语表示协程的一种受限版实现

## 面向对象

### 对操作的接受者(receiver)进行操作

- 可以使用冒号分隔符，相当于隐藏了self这一参数

### 类的实现

- setmetatable（子类，{__index:父类}）

### 继承

- 一种方法类似于js的责任链，或者模板方法模式
- 子类通过__index去查询父类的方法和属性

### 多重继承

- 将一个函数用作__index元方法。

	- 性能不好

- 将被继承的方法复制到子类中

	- 在系统完成后修改方法的定义比较困难
	- 因为修改不会沿着继承层次向下传播

### 私有变量

- lua没有提供私有变量的改变机制

	- 一般用_开头的名称代表私有名称

- 另一种思想是通过两个表来表示一个对象，另一个表用于保存对象的操作（或接口）。我们通过第二个表来访问对象本身。

### 单方法对象

- 直接将单独的方法以对象方式返回即可
- 这个方法也可能是，这个方法其实是一个根据不同的参数完成不同任务的分发方法（dispatch method）

	- 这种非传统的对象实现方式是很高效的，每个对象使用一个闭包，要比单个表的开销更低。

### 对偶表示

- 表示方式

	- key = {}
key[table] = value

- 优缺点

	- 优点

		- 私有性

	- 缺点

		- 如果将一个表作为键，那么这个账户对于垃圾收集器而言就永远也不会编程垃圾，这个账户会留在表中知道某些代码将其从表中显式地删除。

## 输入输出

### 简单IO模型

- write

	- 不推荐io.write(a..b..c) 因为io.write(a,b,c)能用更少的资源完成相同的事情,并且可以避免更多的连接操作

- read

	- 参数

		- "a"

			- 读取整个文件

		- “l”

			- 读取下一行（丢弃换行符）

		- "L"

			- 读取下一行（保留换行符）

		- “n”

			- 读取下一个数值

		- num

			- 以字符串读取num个字符

- output

	- 与input类似，出错会发生异常,如果想直接处理这些异常，必须使用完整I/O模型

- input

	- 调用io.input(filename) 会以只读模式打开指定文件，并将文件设为输入流
	- 除非再次调用io.input

### 完整IO模型

- io.open("文件夹名","模式")

	- 打开文件

- 检查错误  local f = assert(io.open(fileName,modle))

	- 如果出现错误，错误信息会作为 assert 的第二个参数被传入。assert会将错误信息展现出来

- io.lines()

	- 返回一个可以从流打开对应文件的输入流，并在达到文件末尾后关闭该输入流。若调用时不带参数，io.lines就从当前流读取。
	- 从Lua 5.2 开始，函数 io.lines 可以接收和函数io.read一样的参数。

- io.tmpfile()

	- 返回一个操作临时文件的句柄，该句柄是以读/写模式打开的。当程序运行结束后，该临时文件会被自动移除（删除）

- flush

	- 将所有缓冲数据写入文件，可以当做io.flush()使用或者把它当做方法f:flush()使用，以刷新流f。

- setvbuf

	- 用于设置流的缓冲模式。该函数的第一个参数是一个字符串

		- “no”

			- 表示无缓冲

		- “full”

			- 表示在缓冲区满时或者显式地刷新文件时才列入数据

		- “line”

			- 表示输出一直被缓冲直到遇到换行符或从一些特定文件中读取到了数据。

	-  对于后两个选项，函数setvbuf支持可选的第二个参数，用于指定缓冲区大小。

- seek

	- 用来获取和设置文件的当前位置，常常使用f:seek(whence, offset)的形式来调用，其中参数where是指定如何使用偏移的字符串。
	- 当参数wherece取值为“set”时

		- 表示相对于文件开头的偏移

	- 当参数wherece取值为“cur”时

		- 表示相对于当前位置的偏移

	- 当参数wherece取值为“end”时

		- 表示相对于文件结尾的偏移

	- 无论wherce取值是什么，该函数都会以字节为单位，返回当前新位置在流中相对于文件开头的偏移

- os.reaname( )

	- 文件重命名

- os.remove( )

	- 用于移除（删除）文件

- os.getenv( )

	- 获取某个环境变量

		- “HOME”

- os.exec( )

	- 运行系统命令，等价于C语言中的函数system
	- 参数为表示执行命令的字符串，返回值为命令运行结束后的状态。
	- 第一个返回值为布尔类型，当为true时表示程序成功运行完成
	- 第二个返回值是一个字符串，当为“exit”是表示程序正常终结或者终结该程序的信号代码。

- io.popen()

	- 运行一条系统命令，但该函数还可以重定向命令的输入/输出，从而使得程序可以像命令中写入或从命令的输出中读取

- io.type()

	- 检测obj是否是一个可用文件句柄

		- file

			- 打开文件句柄

		- close file

			- 关闭的文件句柄

		- nil

			- 不存在

## 模式匹配

### 模式

- Lua语言中的模式使用百分号作为转义符，所有被转义的字母都具有某些特殊含义，而所有被转移的非字母则表示其本身
- 转义字符

	- .

		- 任意字符

	- %a

		- 字母

	- %b

		- 匹配成对的字符串

			- 如%b()匹配以左括号开始以右括号结束的子串

	- %c

		- 控制字符

	- %d

		- 数字

	- %f

		- 表示前置模式

			- 只有在后一个字符位于char-set内而前一个字符不在时匹配一个空字符串

	- %g

		- 除空格外的可打印字符

	- %l

		- 小写字母

	- %p

		- 标点符号

	- %s

		- 空白字符

	- %u

		- 大写字母

	- %w

		- 字母和数字

	- %x

		- 十六进制数字

	- 大写代表该字符的补集

- 魔法字符

	- ( ) . % + - * ? [ ] ^ $
	- 修饰符

		- +

			- 重复一次或多次

		- *

			- 重复零次或多次

		- -

			- 重复零次或多次（最小匹配）

		- ？

			- 可选（出现零次或一次）

	- ^ 和 $只有在开头和结尾时候表示特殊含义，否则表示本身

### find

- sting.find( str , match)
- 可选参数

	- 第三个参数为索引，从目标字符串哪个位置开始搜索
	- 第四个参数为是否进行简单搜索

- 返回匹配的子串索引

### gsub

- string.gsub(s,n,snp)
- 必选参数 目标字符串、模式和替换字符串

### mathch

- stirng.match(str, match, pattern)

### gmatch

- 返回一个函数，通过返回的函数可以遍历一个字符串中所有出现的指定模式

### 替换

- string.gsub的第三个参数不仅可以是字符串，还可以是一个函数或表

	- 当第3个参数是一个函数时，函数string.gsub会每次找到匹配时调用该函数，参数是捕获到的内容而返回值作为替换字符串
	- 当第3个参数是一个表时，函数string.gsub会把第一个捕获到的内容作为键，然后将表中对应该键的值作为替换字符串。

		- 如果不确定对应的字符串有值，则可以调用tostring函数

### 制表符展开

- 在Lua语言中，像‘()’这样的空白捕获（empty capture）具有特殊意义。该模式并不代表捕获空内容，而是捕获在目标字符串中的位置（该位置是数值）

	- 第2个空捕获的位置是在匹配之后
	- 与find的调用不同

		- print(string.match("hello","()ll()"))   --3 5
print(string.find("hello","ll"))        --3 4

- 对原字符进行替换时，如果字符串中含有转义字符容易出现问题

	- 可先将非字母和数字编码为16进制字符
	- 然后将替换后的字符串解码

## 日期和时间

### os.time()

- 默认获取当前时间
- 如果将table作为参数放入该函数中

	- year, month, day 时段是必须的
	- hour, min sec 没有提供则默认 12:00:00

### os.date()

- 为os.time()的反函数

	- 默认返回字符串
	- 用“*t”参数返回表

- 转义字符

	- %a

		- 星期几的简写

	- %A

		- 星期几的全名

	- %b

		- 月份的简写

	- %B

		- 月份的全名

	- %c

		- 日期和时间

	- %d

		- 一个月的第几天

	- %H

		- 24小时制的小时数

	- %I

		- 12小时制的小时数

	- %j

		- 一年中的第几天

	- %m

		- 月份

	- %M

		- 分钟

	- %p

		- am或pm

	- %S

		- 秒数

	- %w

		- 星期 [0-6 = Sunday-Saturday]

	- %W

		- 一年中的第几周

	- %x

		- 日期

	- %X

		- 时间

	- %y

		- 两位数年份

	- %Y

		- 完整的年份

	- %z

		- 时区

	- %%

		- 百分号

### os.difftime

- 用来计算两个时间之间的差值

## 位运算

### 位运算符

- &

	- 按位与

- |

	- 按位或

- ~

	- 按照位异或

- >>

	- 逻辑右移

- <<

	- 逻辑左移

- ~

	- 按位取反

### 打包和解包二进制数据

- string.pack(modle,arg...)

	- 模式，数据
	- 返回打包后的数据

- string.unpack(modle,data,pos)

	- 模式，数据，坐标（可选）
	- 返回解包后的数据

- 选项

	- 对于size_t而言还有一个额外的选项T
	- 可以用三种形式打包字符串

		- z

			- \0结尾的字符串

		- cn

			- 定长字符串，n为被打包字符串的字节数

		- sn

			- n用于刨槽字符串长度的无符号整型数的大小

	- 整型

		- b

			- char

		- h

			- short

		- i

			- int

		- l

			- long

		- j

			- lua中整型数的大小

		- 每一个参数都有一个对应的大写版本，对应相应大小的无符号整型数。

	- 浮点型

		- d

			- 单精度浮点数

		- f

			- 双精度浮点数

		- n

			- lua浮点数

- 可以在选项i后加上一个1~16的数，如i7会产生7字节的整型数字，所有的大小都会被检查是否存在溢出的情况
- 使用>选项把后续的编码转换为大端模式或网络字节序列(network byte order)
- 使用<选项改为小端模式
- 使用= 选项改回机器默认的原生大小端模式

## 数据文件和序列化

### 使用函数string.format的“%q”选项，设计为一种能够让lua语言安全地反序列化字符串的方式序列化字符串，它使用双括号括住字符串并正确地转义其中的双引号和换行符等其他字符。

### Lua 5.3.3 对“%q” 进行了扩展，使其也可以用于数值，nil和Boolean类型

## 垃圾收集

### 通过设置__mode可以将键值变为弱引用

- k

	- 键

- v

	- 值

- kv

	- 键值

### 垃圾收集指令

- collectgarbage()

### 记忆函数

- 空间换时间是常用的技巧
- 使用弱引用表来进行段时间的记忆（缓存），可以防止服务器被过多的缓存导致的内存耗尽。

### 具有默认值的表

- 第一种方法

	- 使用一个弱引用表映射每一个表和它的默认值
	- 键为弱引用
	- 适用于默认元素较少的情况

- 第二种方法

	- 对默认值使用不同的元表，在遇到重复的默认值会复用相同的元表
	- 值为弱引用
	- 适用于默认元素较多的情况

### 瞬表（5.1引入）

- 当一个具有弱引用键的表中的值又引用了对应的键
- 在Lua语言中，一个具有弱引用键和强引用值的表是一个瞬表。在一个瞬表中，一个键的可访问性控制这对应值的可访问性。
- 解决方法

	- 常量函数工厂

### 析构器

- Lua语言通过元方法__gc实现析构器
- 如果不提前把元表的__gc方法设置，则没有办法让lua知道析构函数

	- 可以通过提前设置标记的方法，将__gc先赋一个任意值作为占位符。

- 关联不会影响对象析构的顺序
- 复苏

	- 当一个析构器被调用时，它的参数是正在被析构的对象。因此，这个对象会至少在析构期间重新变成活跃的。（临时复苏）
	- 在析构器执行期间，我们无法阻止析构器把该对象存储在全局变量中，使得该对象在析构器返回后仍然可访问。（永久复苏）

- 析构器阶段

	- 当垃圾收集器首次发现某个具有析构器的对象不可达时，垃圾收集器就把这个对象复苏并放到等待被析构的队列中。
	- 一旦析构器开始执行，lua语言就将该对象标记为已被析构。当下一次垃圾收集器又发现这个对象不可达时，它就将这个对象删除。
	- 如果为了确保程序中的垃圾都被删除了，那么必须调用collectgarbage两次。

### 垃圾收集阶段

- 全局暂停式垃圾收集器（stop the world）(5.0及之前)

	- 标记

		- 从根节点集合（Lua可以直接访问的对象）进行可达性标记，标记为活跃

	- 清理

		- 处理析构器和弱引用表
		- 遍历所有标记为需要进行析构、但有没有被标记为活跃状态的对象。
		- 没有被标记为活跃状态的对象会被标记为活跃（复苏，resurrected），并被放在一个单独的列表中，这个列表会在析构阶段用到。

	- 清除

		- 遍历所有对象（Lua把所有对象放在一个链表中）如果一个对象没有被标记为活跃，Lua语言就将其回收。否则，Lua语言清理标记，然后准备进行下一个清理周期

	- 析构

		- Lua语言调用清理阶段被分离出的对象的析构器

- 增量式垃圾收集器(incremental collector)

	- 与全局式使用相同的步骤
	- 当解释器分配了一定数量的内存时，垃圾收集器也执行一小步（这意味着，在垃圾收集工作期间，解释器可能会改变一个对象的可达性。为了保证垃圾收集器的正确性，垃圾收集器中的有些操作具有发现危险改动和纠正设计对抓了标记的内存屏障）

- 紧急垃圾收集（emergency collection）

	- 当内存分配失败时，Lua语言会强制进行一次完整的垃圾收集，然后再次尝试分配。
	- 这些收集动作不能运行析构器

### 控制垃圾收集的步长

- 参数

	- 可选字符串，用来说明进行何种操作
	- 选项

		- stop

			- 停止垃圾收集器，直到使用选项“restart”再次调用collectgarbage.

		- restart

			- 重启垃圾收集器

		- collect

			- 执行一次完整的垃圾收集，回收和析构所有不可达的对象

		- stop

			- 执行某些垃圾收集工作，第二个参数data指明工作量，即在分配了data个垃圾收集器应该做什么

		- count

			- 以KB为单机返回当前已用内存数，该结果是一个浮点数，乘以1024得到的就是精确的字节数。该值包括了尚未回收的死对象。

		- setpause

			- 设置收集器的pause参数（间歇率）。参数data以百分比为单位给出要设定的新值
			- 当data为100时，参数被设定为1（100%）

		- setstepmul

			- 设置收集器的stepmul参数（步进倍率，step multiplier）。 
			- 参数data给出新值，也是以百分比为单位

- 作用

	- pause

		- 当值为200%时，表示在重启垃圾收集器前等待内存使用翻番。
		- 当值为0时，lua语言在上一次垃圾回收结束后立即开始一次新的收集
		- 如果想消耗更多的CPU时间换取更低的内存消耗，那么可以把这个值设得小一点。
		- 通常这个值设在0到200%之间

	- setmul

		- 控制对于每分配1KB内存，垃圾收集器应该进行多少工作。这个值越高，垃圾收集器使用的增量越小
		- 默认值为200%
		- 低于100%的值会让收集器运行得很慢，以至于可能一次收集也完不成

