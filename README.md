# 说明

博客采用 hexo 框架+原版仙人掌主题
仙人掌主题：https://probberechts.github.io/hexo-theme-cactus/

# 链接

博客已同步至 vercel(推荐使用该路线，hexo url 已重定向到 vercel)
|路线|链接|
|---|---|
|github 路线(blog)|[https://gubaiovo.github.io/](https://gubaiovo.github.io/)|
|vercel 路线(主页)|[https://www.gubaiovo.com/](http://www.gubaiovo.com/)|
|vercel 路线(blog)|[https://blog.gubaiovo.com/](https://blog.gubaiovo.com/)|

# 同步 Vercel 教程

## 导入

在 [Vercel](https://vercel.com/) 登录 github 后导入 github 库即可，使用该主题的话，Framework Preset 要选择 Other。导入后会自动生成 `.vercel.app` 域名，该域名国内已经被墙。

在 github 的修改都会同时同步到 vercel，不需要在 vercel 再配置一遍 git。

## 自定义域名

可以使用自定义域名（**首先你要有个域名**）加速访问。在 Vercel 的博客项目中的 `Settings` 里的侧边栏有 `Domains` 设置，在输入栏输入自定义域名后 `Add` 提示 `Invalid Configuration`，下面会显示解析需要的类型和值。

如果提示的解析类型是 `CNAME` (我这里是这样的)，值为 `cname.vercel-dns.com`，那么在域名服务商添加解析时需要把值修改为 `cname-china.vercel-dns.com`
