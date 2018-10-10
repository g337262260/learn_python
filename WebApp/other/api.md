## API

后端API包括：

获取日志：GET /api/blogs      ok

创建日志：POST /api/blogs     ok

修改日志：POST /api/blogs/:blog_id  ok 

删除日志：POST /api/blogs/:blog_id/delete    ok  

获取评论：GET /api/comments          ok

创建评论：POST /api/blogs/:blog_id/comments      ok

删除评论：POST /api/comments/:comment_id/delete          ok

创建新用户：POST /api/users       ok

获取用户：GET /api/users        ok     

管理页面包括：

评论列表页：GET /manage/comments      ok

日志列表页：GET /manage/blogs         ok

创建日志页：GET /manage/blogs/create      ok

修改日志页：GET /manage/blogs/            ok

用户列表页：GET /manage/users         ok

用户浏览页面包括：

注册页：GET /register    ok  
        
登录页：GET /signin     ok 

注销页：GET /signout    ok

首页：GET /                ok

日志详情页：GET /blog/:blog_id     ok