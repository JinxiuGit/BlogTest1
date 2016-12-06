#BlogTest1
##brief introduction
MyFirstProject is a django project. It describes a simple blog.
_ _ _
##fundamental function
There are three html files in templates.
> **homepage.html:** include all blogs and their urls
**blogDisplay.html:** display specific blog
**aboutMe.html:** get something about author when you click on the author "fireworm" on homepage
_ _ _
##how the blog response
> - Firstly, we make the definition of data structure also tables in the file
  "myblog/models.py" 
> - Secondly, we configurate some urls corresponding to specific function in the
  file "MyFirstProject/urls.py"
> - Thirdly, we finish concrete context related to different pages in the file
  "myblog/tempaltes/\*\.html"
> - Finally, we draw the page using functions in the file "blog/views.py"

*On the whole, the functions of the file "views.py" find the specfic html file from the folder "templates" and then jump to the homologous url of file "urls.py" to response the client.*
_ _ _
###**Welcome to discuss problems with [me](https://github.com/JinxiuGit).:blush:**
