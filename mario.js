
printPyramid(5);


/*
 * printPyramid
 *
 * Prints to the console a pyramid of '#' characters of the specified height
 * For example, if height is 5, the console will look like this:
 *          ##
 *         ###
 *        ####
 *       #####
 *      ######
 */
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
        console.log(str);
        firstSharpCounter++;
    }
    drawPyramid(height);
}

function drawPyramid(height, symbol = 'box') {
    document.getElementById("pyramid").innerHTML = "";
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
        var para = document.createElement("p");
        para.style.margin = "0px";
        para.innerHTML = str;
        document.getElementById("pyramid").appendChild(para);
        firstSharpCounter++;
    }
}