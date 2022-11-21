# MySQL 必知必会

## 命令

### 数据库操作

- 选择数据库

	- USE 数据库名

- 显示所有数据库

	- SHOW DATABASES

- 显示所有表

	- SHOW TABLES

- 显示表的列

	- SHOW COLUMNS FROM customers

- 显示服务器信息

	- SHOW STATUS

- 显示创建数据库/表的信息

	- SHOW CREATE DATABASE/TABLE

- 显示授予用户(所有或者特定)的安全权限

	- SHOW GRANTS

- 显示服务器错误或者警告信息

	- SHOW ERRORS/WARNINGS

### 查询

- 结构

	- SELECT (DISTINCT) (表名.)列名

		- DISTINCT 

			- 返回唯一值

		- 表名.

			- 可在歧义的时候使用

		- 执行算术运算
		- 函数

			- 函数一般移植性不强，几乎每种主要的DBMS的实现都支持其它实现不支持的函数，而且有时差异还很大。
			- 文本处理函数

				- Concat()

					- 拼接(concatenate) 将值联结到一起构成单个值
					- 多数DBMS使用 + 或 || 来实现拼接

				- Trim()

					- 去除空格
					- 有LTrim(), RTrim(), Trim() 三种

				- Upper()

					- 转换为大写

				- Left()

					- 返回串左边的字符

				- Length()

					- 返回串的长度

				- Locate()

					- 找出串的一个子串

				- Lower()

					- 将串转换为小写

				- Right()

					- 返回串右边的字符

				- SubString()

					- 返回子串

				- Soundex()

					- 返回串的SOUNDEX()值
					- 能够检查拼写相近的单词

			- 时间和日期处理函数

				- AddDate()

					- 增加一个日期(天，周等)

				- AddTime()

					- 增加一个时间(时，分等)

				- CurDate()

					- 返回当前日期

				- CurTime()

					- 返回当前时间

				- Date()

					- 返回日期时间的日期部分

				- DateDiff()

					- 计算两个日期之差

				- Date_Add()

					- 高度灵活的日期运算函数

				- Date_Format()

					- 饭后一个格式化的日期或时间串

				- Day()

					- 返回一个日期的天数部分

				- DayOfWeek()

					- 对于一个日期，返回对应的星期几

				- Hour()

					- 返回一个时间的小时部分

				- Minute()

					- 返回一个时间的分钟部分

				- Month()

					- 返回一个日期的月份部分

				- Now()

					- 返回当前日期和时间

				- Time()

					- 返回一个日期时间的时间部分

				- Year()

					- 返回一个日期的年份部分

			- 数值处理函数

				- Abs()

					- 绝对值

				- Cos()

					- 余弦

				- Exp()

					- 指数

				- Mod()

					- 余数

				- Pi()

					- 圆周率

				- Road()

					- 随机数

				- Sin()

					- 正弦

				- Sqrt()

					- 平方根

				- Tan()

					- 正切

			- 聚集函数

				- AVG()

					- 返回某列的平均值

				- COUNT()

					- 返回某列行数

				- MAX()

					- 返回某列最大值

				- MIN()

					- 返回某列最小值

				- SUM()

					- 返回某列之和

				- 默认是ALL 可指定DISTINCT

	- FROM 表
	- WHRER 条件

		- 条件运算符

			- =

				- 等于

			- <>

				- 不等与

			- !=

				- 不等于

			- <

				- 小于

			- <=

				- 小于等于

			- >

				- 大于

			- >=

				- 大于等于

			- BETWEEN

				- 在指定的两个值之间

		- 组合子句

			- AND 操作符

				- AND 优先级更高

			- OR 操作符
			- NOT 操作符

				- 用来否定后跟的条件关键字

			- LIKE 操作符

				- 使用通配符

					- 通配符

						- 用来匹配值的一部分的特殊字符
						- %

							- 任意字符出现任意次数

						- _

							- 任意字符单个字符

					- 搜索模式

						- 由字面量、通配符或两者组合构成的搜索条件

			- REGEXP

				- 正则表达式
				- 预定义字符集

					- [:alumn:]

						- 任意字母和数字

					- [:alpha:]

						- 任意字符

					- [:blank:]

						- 空格和制表

					- [:cntrl:]

						- ASCII控制字符 (0-31,127)

					- [:digit:]

						- 任意数字

					- [:lower:]

						- 任意小写字母

					- [:print:]

						- 任意可打印字符

					- [:punct:]

						-  既不在[:alnum:]又不在[:cntrl:]中的任意字符

					- [:space:]

						- 包括空格在内的任意空白字符

					- [:upper:]

						- 任意大写字母

					- [:xdigit:]

						- 任意16进制数字

			- IN 操作符

				- 指定条件范围
				- 优点

					- 在使用长的合法选项清单时，IN操作符的语法更清楚且更直观
					- 在使用IN时，计算的次序更容易管理(因为使用的操作符更少)
					- IN操作符一般比OR操作符清单执行更快
					- IN的最大优点是可以包含其他SELECT语句，使得能够更动态地建立WHERE语句

			- CASE函数

				- 简单CASE函数

					- CASE 列
    WHEN 值 THEN 结果
    WHEN 值 THEN 结果
    ELSE '其他' END

				- CASE搜索函数

					- CASE WHEN 条件 THEN 结果
    WHEN 条件 THEN 结果
    ELSE 其它 END

	- GROUP BY 分组 HAVING 分组过滤条件

		- HAVING 和 WHERE区别

			- WHERE 在数据分组前进行过滤
			- HAVING在数据分组后进行过滤

	- ORDER BY 列名

		- ASC

			- 正序，一般省略

		- DESC

			- 倒序

	- LIMIT 数字,数字

		- 可指定要检索的开始行和行数
		- 索引从0开始
		- 可使用 LIMIT 数字 OFFSET 数字 来避免歧义

- UNION 组合查询

	- 规则

		- UNION必须由两条或者两条以上的SELECT语句组成,语句之间用关键字UNION分隔。
		- UNION中的每个查询必须包含相同的列、表达式或聚集函数。
		- 列数据类型必须兼容：类型不比完全相同，但必须是DBMS可以隐含转换的类型。

	- UNION从结果集中自动去除了重复的行，如果需要，可以使用UNION ALL 返回所有行

- 全文本搜索

	- 并不是所有引擎都支持全文搜索

		- MyISAM支持全文搜索
		- InnoDB不支持全文搜索

	- 普通文本搜索和基于正则表达式的限制

		- 性能
		- 明确控制

			- 很难明确控制匹配什么和不匹配什么

		- 智能化的结果

			- 不能提供一种智能化的结果选择方法

	- 启用全文本搜索

		- 在创建表时指定FULLTEXT

	- 语法

		- Match(列名) Against('内容')

			- 可在内容后加上WITH QUERY EXPANSION 实现查询扩展
			- 查询扩展越相关的行排名越靠前

		- Match(列名) Against('内容', IN BOOLEAN MODE)

			- 布尔文本搜索内容

				- 要匹配的词
				- 要排斥的词
				- 排列显示
				- 表达式分组
				- 另外一些内容

			- 全文本布尔操作符

				- +

					- 包含，词必须存在

				- -

					- 排除，词必须不出现

				- >

					- 包含，而且增加等级值

				- <

					- 包含，而且减少等级值

				- ()

					- 把词组成子表达式

				- ~

					- 取消一个词的排序值

				- *

					- 词尾的通配符

				- ""

					- 定义一个短语

			- 即使没有定义FULLTEXT索引，也可以使用它

### 插入

- 语法

	- INSERT INTO 表名(列名)
	- VALUES(数据),(数据);

- 查看自增主键上次插入的数据

	- SELECT last_insert_id();

### 更新数据

- 语法

	- UPDATE 表名

		- 可在UPDATE 后使用IGNORE关键字，用于忽略更新过程中的错误，否则会产生回滚

	- SET 列= 内容
	- WHERE 条件

- UPDATE与安全

	- 可以限制和控制UPDATE的使用

### 删除数据

- 语法

	- 传统删除

		- DELETE FROM 表名
		- WHERE 条件

	- 快速删除并清除自增（不可回滚）

		- truncate table 表名

### 表操作

- 创建表

	- CREATE TABLE 表名
	- (列名 类型 约束)
	- 引擎，字符设定
	- 常见引擎

		- InnoDB

			- 是一个可靠的事务处理引擎，它不支持全文搜索

		- MEMORY

			- 在功能上等同于MyISAM,但由于数据存储在内存中，速度很快(适合用于临时表)

		- MyISAM

			- 是一个性能极高的引擎，它支持全文本搜索，但不支持事务处理

- 更新表

	- ALTER TABLE 表名
	- 操作

		- ADD

			- 列
			- 约束

		- DROP

			- 列 列名

	- 一般复杂表的操作分为

		- 创建新表
		- 将旧表数据INSERT SELECT 到新表中
		- 检验包含所需数据的新表
		- 重命名旧表
		- 用旧表原来的名称重命名新表
		- 根据需要，重新创建触发器、存储过程、索引和外键

- 删除表

	- DROP TABLE 表名
	- 重命名表

		- RENAME TABLE 旧名称 TO 新名称

- 创建索引

	- CREATE INDEX 索引名
	- ON 表名 (列 [ASC|DESC])

### 视图

- 使用规则和限制

	- 视图必须唯一命名
	- 对于可以创建的视图数目没有限制
	- 为了创建视图，必须具有足够的访问权限。
	- 视图可以嵌套，即可以利用从其它视图中检索数据的查询来构造一个视图。
	- ORDER BY 可以用在视图中，但如果从该视图检索数据SELECT中也含有ORDER BY ，那么该视图中的 ORDER BY 将被覆盖。
	- 视图不能索引，也不能有关联的触发器或默认值。
	- 视图可以和表一起使用

- 语法

	- CREATE VIEW 视图名 AS 
	- 查询语句

### 存储过程

- 使用理由

	- 通过把处理封装在容易使用的单元中，简化复杂的操作
	- 由于不要求反复锦江城一系列处理步骤，者保证了数据的完整性
	- 简化对变动的管理
	- 提高性能
	- 存在一些只能用在单个请求中的MySQL元素和特性，存储过程可以使用它们来编写更强更灵活的代码。

- 缺陷

	- 存储过程的编写比基本SQL语句复杂
	- 你可能没有创建存储过程的安全访问权限。徐国数据库管理员限制存储过程的创建权限，允许用户使用存储过程，但不允许他们创建存储过程。

- 调用存储过程

	- CALL 存储过程(@参数)
	- 存储过程可以显示结果，也可以不显示结果

- 删除存储过程

	- DROP PROCEDURE 存储过程名

### 游标

- 不同于多数DBMS，MySQL游标只能用于存储过程(和函数)
- 语法

	- 定义

		- 在存储过程中 DECLARE 游标名 CURSOR

	- 打开

		- OPEN 游标名

	- 关闭

		- CLOSE 游标名
		- MySQL 会在到达END 后自动关闭游标

### 触发器

- 仅支持表

	- 只有表才支持触发器，视图不支持，临时表也不支持

- BEFORE 和AFTER

	- 通常将BEFORE用于数据验证和净化

- 创建触发器

	- CREATE TRIGGER 触发器名称 操作时间 ON 操作表 
	- FOR EATCH ROW 是对每个插入的行显示一次

### 事务

- 术语

	- 事务 ( transatction )

		- 指一组SQL语句

	- 回退( rollback )

		- 指撤销指定SQL语句的过程

	- 提交( commit )

		- 指将未存储的SQL语句结果写入数据库表

	- 保留点( savepoint )

		- 指事务处理中设置的临时占位符 (  place-holder ) , 你可以对它发布回退。

- 语法

	- START TRANSACTION
	- SAVEPOINT 保留点名称
	- TOLLBACK TO 保留点名称
	- COMMIT;

### 全球化和本地化

- 术语

	- 字符集

		- 字母和符号的集合

	- 编码

		- 为某个字符集成员的内部表示

	- 校对

		- 为规定字符如何比较的命令

- 语法

	- 查看字符集和校对

		- SHOW VARIABLES LIKE 'character%'
		- SHOW VARIABLES LIKE 'collation%'

	- 设置字符集和校对

		- CHARACTER SET 字符集名称
		- COLLATE 校对名称

### 安全管理

- 管理用户

	- 查看用户

		- USE mysql
		- SELECT user FROM user;

	- 创建账号

		- CREATE USER 用户名 IDENTIFIED BY 密码

	- 重命名用户

		- RENAME USER 旧用户名 TO 新用户名

	- 删除用户

		- DROP USER 用户名

- 权限管理

	- 查看权限

		- SHOW GRANTS FOR 用户名

	- 设置权限

		- GRANT 权限 ON 数据库.表(*) TO 用户名

	- 撤销权限

		- REVOKE 权限 ON 数据库.表(*) FROM 用户名

- 权限列表

	- ALL

		- 除GRANT OPTION 外的所有权限

	- ALTER

		- 使用 ALTER TABLE

	- ALTER ROUTINE

		- 使用 ALTER PROCEDURE 和 DROP PROCEDURE

	- CREATE
	- CREATE ROUUTINE 
	- CREATE TEMPORARY TABLE
	- CREATE USER

		- 使用CREATE USER 、DROP USER、 RENAME USER 和 REVOKE ALL PRIVILEGES

	- CREAT VIEW
	- DELETE
	- DROP

		- 使用 DROP TABLE

	- EXECUTE

		- 使用CALL 和次数过程

	- FILE

		- 使用 SELECT INTO OUTFILE 和 LOAD DATA INFILE

	- GRANT OPTION

		- 使用GRANT 和 REVOKE

	- INDEX

		- 使用CREATE INDEX 和 DROP INDEX

	- INSERT
	- LOCK TABLES
	- PROCESS

		- 使用 SHOW FULL RPOCESSLIST

	- RELOAD

		- 使用FLUSH

	- REPLICATION CLIENT

		- 从服务器位置访问

	- REPLICATION SLAVE

		- 复制从属使用

	- SELECT
	- SHOW DATABASES
	- SHOW VIEW
	- SHUTDOWN

		- 使用mysqladmin shutdown

	- SUPER

		- 使用CHANGE MASTER 、KILL、LOGS、RURGE、MASTER 和SET GLOBAL。还允许mysqladmin调试登录。

	- UPDATE
	- USAGE

		- 无访问权限

## 建议

### 改善性能

- 一般来说，关键的生产DBMS应该运行在自己的专用服务器上。
- MySQL是用一系列的默认设置预先配置的，从这些开始通常是很好的。但过一段时间后你可能需要调整内存分配、缓冲区大小等。
- MySQL是一个多用户多线程的DBMS，换言之，它经常同时执行多个任务。如果这些任务中的某一个请求执行缓慢，则所有请求都会执行缓慢。

	- 如果遇到显著的性能不良，可使用SHOW PROCESS LIST 显示所有或多进程。
	- 还可以用KILL命令中介某个特定的进程

- 总是有不止一种方法编写同一条SELECT语句。应该实验联结，并、子查询等，找出最佳的方法。
- 使用 EXPLAIN 语句让 MySQL 解释它将如何执行一条SELECT 语句。
- 一般来说，存储过程执行得比一条条地执行其中各条MySQL语句快。
- 应该总是使用正确的数据类型
- 决不要检索比需求还要多的数据。换言之，不要用SELECT * (除非你真正需要每个列)
- 有的操作(包括 INSERT ) 支持一个可选的 DELAYED 关键字, 如果使用它，将把控制立即返回给调用程序，并且一旦有可能就执行该操作。
- 在导入数据时，应该关闭自动提交。可能你还想删除索引(包括 FULLTEXT 索引 )，然后在导入完成后重建它们。
- 必须索引数据库表以改善数据库检索的性能。确定索引不是什么一件微不足道的任务，需要分析使用的SELECT语句以找出重复的WHERE 和 ORDER BY 子句。如果一个简单的 WHERE 子句返回结果所花的事件太长，则可以断定其中使用的列(或几个列)就是需要索引的对象。
- 你的SELECT 语句中有一系列复杂的OR条件吗？通过使用多条SELECT语句和连接它们的UNION语句，你能看到极大的性能改进。
- 索引改善数据检索的性能，但损害数据插入、删除和更新的性能。如果你有一些表，他们收集数据且不经常需要被搜索，则在有必要之前不需要索引它们。
- LIKE 很慢。 一般来说，最好是使用FULLTEXT 而不是LIKE。
- 数据库是不断变化的尸体，一组优化良好的表一会儿后可能就面目全非了。由于表的使用和内容的更改，理想的优化和配置也会改变。
- 最终重要的规则就是，没调规则在某些条件下都会被打破。

