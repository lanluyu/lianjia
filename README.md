lianjia说明文档
==
介绍
 - 
lianjia是一个基于Scrapy的深圳二手房信息爬虫，爬取了链家网的所有深圳二手房信息。<br>

代码说明
--
### 运行环境
* Windows 10 专业版<br>
* Python 3.5/Scrapy 1.5.0/MongoDB 3.4.7<br>

### 依赖包
* Requests<br>
* Pymongo<br>
* Faker(随机切换User-Agent)<br>

### 其它
在分析链家网深圳二手房页面的时候，显示总共有24891条二手房信息。但其页面显示规律是一页显示30条信息，最大页数为100，总数为3000。此时，如果按照常规的爬取方法就无法获取全部的数据。继续分析发现，可以按照二手房的不同价格，位置来分类，保证该分类下显示的二手房信息数小于3000，这样就可以获取该分类的全部信息。然后在同分类下再选取其它条件，就可以保证覆盖全部二手房了。<br>
这里我选取了房屋总价和楼层高低相结合的条件来分类爬取，保证了每一类的总数是小于3000的。爬虫里面相应的处理各分类页面的链接时，注意一下链接地址和其对应的最大页面即可。链家网唯一的防爬措施似乎就是这个，利用最大页面的限制来防止爬虫爬取过多的信息。

爬取结果
-
在链家深圳二手房页面共获取了23224条个股信息。因为其中有部分发页面是以移动端页面显示的，这样就造成提取规则不适合，所幸此页面比较少，不然就要改用爬取移动端页面的方法获取信息了。每条信息中包括了该二手房的详细信息。结果由爬虫先存储在MongoDB中，再导出为Excle文件。部分数据如下截图:<br>
![房产信息截图](https://github.com/lanluyu/lianjia/blob/master/%E4%BA%8C%E6%89%8B%E6%88%BF%E4%BF%A1%E6%81%AF%E6%88%AA%E5%9B%BE.PNG)
