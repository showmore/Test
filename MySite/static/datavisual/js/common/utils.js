var func = (function (func) {
    /*随机产生数据*/
    func.randomData = function () {
        return Math.round(Math.random() * 100);
    };

    return func;
})(func || {});