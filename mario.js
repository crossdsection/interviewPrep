
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
}
