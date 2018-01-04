/**
 * Created by Administrator on 2017-08-28.
 */

$(function(){

    var nav=$(".nav"); //得到导航对象

    var win=$(window); //得到窗口对象

    var sc=$(document);//得到document文档对象。

    win.scroll(function(){
        if(sc.scrollTop()>=1){
        nav.addClass("fix");
        }
        else{nav.removeClass("fix");
        }
});
});



$(function(){
        $("th").click(function(){
            $(this).css("color","greenyellow");
        })
    })

$(function(){
    $(".list-group-item").click(function(){
          $(".dlt1").slideToggle("slow");
        })
})


