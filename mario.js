
$(document).ready(function(){
    printPyramid($("#bricksCount").val());
    $("#symbol").on('change', drawPyramid);
    $("#bricksCount").on('change', drawPyramid);

    function printPyramid(height) {
        firstSharpCounter = 2;
        for( var j = 0; j < height; j++ ) {
            var str = '';
            for( var i = height; i >= 0; i--) {
                if( i < firstSharpCounter ) {
                    str+= '#';
                } else {
                    str+= ' ';
                }
            }
            firstSharpCounter++;
        }
        drawPyramid(height);
    }

    function drawPyramid(height, symbol = 'box') {
        height = $("#bricksCount").val();
        symbol = $("#symbol").val();

        $("#pyramid").html('');
        firstSharpCounter = 2;
        for( var j = 0; j < height; j++ ) {
            var str = '';
            for( var i = height; i >= 0; i--) {
                if( i < firstSharpCounter ) {
                    str+= (symbol == 'box' ) ? '<div style="display:inline-block;width:40px;height:40px;background:#820000;border:2px solid;border-color:#eeeeee;"></div>' : symbol;
                } else {
                    str+= (symbol == 'box' ) ? '<div style="display:inline-block;width:40px;height:40px;background:#eeeeee;border:2px solid;border-color:#eeeeee;"></div>' : "&nbsp;";
                }
            }
            let para = $("<p>");
            para.css({margin:0});
            console.log(para);
            $("#pyramid").append(para);
            para.html(str);
            firstSharpCounter++;
        }
    }

});