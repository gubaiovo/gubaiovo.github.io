```text
---
layout:     post
title:      从 0 → int a = INT_MIN - 1 成为CTFer
subtitle:   CTF
date:       2024-10-10
author:     顾白
header-img: img/the-first.png
catalog:   true
tags:
    - CTF
---
```

# 从 0 → int a = INT_MIN - 1 成为CTFer

## whoami

在大学之前，我对信息安全的理解仅限于电影、小说中的hacker。直到参加了NewStar CTF 2024，才开始逐渐接触真正的信安技术。决定通过这个栏目记录自己在 CTF 的每个印记。

## per

对于0基础的CTFer，通篇浏览[CTF WIKI](https://ctf-wiki.org/) 是很有必要的，可以先忽略掉具体的解题步骤、题目分析，只需要了解CTF是什么，CTF有哪些种类等等。

在一切开始之前，非常推荐学习 ***linux*** ，初学只需要了解基础命令即可。在实战中，linux 将会是解题一大利器。我使用的是 [kali](Kali Linux，是linux发行版之一，拥有很多安全工具 "什么是kali？") 虚拟机，未来的 [wp](WriteUp，指题解 "什么是wp？") 中会经常看到linux的身影。

除了 linux，一个趁手的文本编辑工具也是很有必要的。这里推荐*** [vscode](https://code.visualstudio.com/)***，vscode本身就是很强大的文本编辑器，各种插件加持后功能非常强大。如果你使用了 vmware 的虚拟机，或者使用了远程服务器，vscode的ssh插件可以提供连接功能。~~vmware太卡了~~

CTF 还有非常多的工具，这些后面再谈。

如果你需要写wp，可以尝试 [markdown](https://markdown.com.cn/) 语法，一种非常简单且易学的语法(本人从学习markdown到开始写blog仅用了不到半小时)。使用语法需要合适的编辑器，这里推荐 [Typora](https://typoraio.cn/)  ，一款轻量且支持实时预览的 markdown编辑器。~~pwn？自寻！~~

软件支持之外，最好是掌握一门编程语言，这里推荐 ***python***，python语法简单，库非常丰富。不需要非常精通python，但基础的数据类型、语法结构等内容要大概了解一下。blog中具体python脚本将会逐行注释。

当然，如果你有更趁手的语言，可以不考虑py，但最好了解一些上述python基本内容，这样也更方便将网络资源中的py脚本转换为你所熟悉的脚本。但涉及第三方类库时就是对你的能力的考验了。编程语言多多益善。你所掌握的每一门编程语言，无论在哪里都会发光的！

学习编程语言在CTF中还有另一个作用，对于一些同类型题目，可以自己编写工具脚本通杀同类。这是为自己铸剑的过程。当你自己的工具脚本数量足够多，你的编程水平也会有很大的飞跃。

最后，不要沉浸于通过脚本、工具得到flag的喜悦中(脚本小子是被安全领域唾弃的)，成为优秀的CTFer需要深挖安全问题背后的原理。

## end

安全领域永无止境，CTF 的几大方向中建议专精某些个方向。善用搜索引擎(google, bing)以及ai (chatgpt、fitten code、通义、github copilot等等)。遇到问题先自己捣鼓1h再虚心请教他人。多多学习各个工具的用法。至此，你已经具备了成为CTFer的基本素养。

> Talk is cheap. Show me the flag.

<p align="right">2024.10.10</p>

<p align="right">Writen by 顾白</p>





​	