window.onload=function(){
    const hamburger = document.querySelector('.hamburger');

hamburger.addEventListener('click', function () {
    this.classList.toggle('is-active');
});

hamburger.addEventListener('click', function () {
    document.querySelector('.menu-hide').classList.toggle('is-active');
});}

function LikeiRefresh(url) {
    $.ajax({
        type: "GET",
        url: url,
        dataType: "html",   // 期待后端返回数据的类型
        success: function (data) {//返回数据根据结果进行相应的处理
            $("#navigation-2").html(data);
        },
        error: function () {
            $("#navigation-2").html("获取数据失败！");
        }
    });
}

function LikevRefresh(url) {
    $.ajax({
        type: "GET",
        url: url,
        dataType: "html",   // 期待后端返回数据的类型
        success: function (data) {//返回数据根据结果进行相应的处理
            $("#navigation-1").html(data);
        },
        error: function () {
            $("#navigation-1").html("获取数据失败！");
        }
    });
}

function alert(url) {
    $.ajax({
        type: "GET",
        url: url,
        dataType: "html",   // 期待后端返回数据的类型
        success: function (data) {//返回数据根据结果进行相应的处理
            $("#alert").html(data);
        },
        error: function () {
            $("#alert").html("获取数据失败！");
        }
    });
}


(function($){
	/*------------------
  		HEADER
  	--------------------*/

	$(window).on('scroll resize',function(e) {
		if ($(this).scrollTop() > 70) {
			$('.header-section').removeClass('sticky');
		}else{
			$('.header-section').addClass('sticky');
		}
		e.preventDefault();
	});

	})(jQuery);