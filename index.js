let pixelBorder = 1;
let pixelSize = 20;
let canvasHeight = 500;
let palletWidth = 100;
let currentlyColor = "purple";

const sampleColorArray = ["#ffffff","#68b0ab","#006a71","#ff7e67","#d789d7","#1a1c20"];

function createPallet() {
    let palletElem = document.getElementById("pallet");
    palletElem.style.width = palletWidth + "px";

    let inputDiv = document.createElement("div");
    let colorPallet = document.createElement("input");
    colorPallet.setAttribute("type", "color");
    colorPallet.addEventListener("change", function(cc) {
        currentlyColor = colorPallet.value;
    });

    inputDiv.appendChild(colorPallet);
    palletElem.appendChild(inputDiv);

    for( const color of sampleColorArray ) {
        let inputDiv = document.createElement("div");
        inputDiv.style.width = "50px";
        inputDiv.style.margin = "25px";
        inputDiv.style.border = "1px solid";
        inputDiv.style.height = "50px";
        inputDiv.style.background = color;
        inputDiv.addEventListener("click",function(){
            currentlyColor = color;
        });
        palletElem.appendChild(inputDiv);    
    }
}

createPallet()

function createCanvas() {
    let canvasElem = document.getElementById('canvas');
    let widthAvailable = canvasElem.parentNode.offsetWidth - palletWidth;
    canvasElem.style.width = widthAvailable + 'px';
    canvasElem.style.height = canvasHeight + 'px';
    
    let numberOfRows = Math.round(canvasHeight / (pixelSize + pixelBorder * 2));
    let numberOfCols = Math.round(widthAvailable / (pixelSize + pixelBorder * 2)) - 5;

    for( let i = 0; i < numberOfRows; i++ ) {
        var row = document.createElement("div");
        row.setAttribute("id", "row_" + (i+1));
        row.style.width = widthAvailable + 'px';
        row.style.height = (pixelSize + pixelBorder * 2) + 'px';
        for( j = 0; j < numberOfCols; j++ ) {
            var pixel = document.createElement("div");
            pixel.setAttribute("id", "row_" + (i+1) + "_" + (j+1));
            pixel.style.width = pixelSize + 'px';
            pixel.style.height = pixelSize + 'px';
            pixel.style.display = 'inline-block';
            pixel.style.background = '#ffffff';
            pixel.style.border = '1px solid';
            pixel.addEventListener('ondragstart', function() {return false;});
            pixel.addEventListener('mousedown', downPixel);
            pixel.addEventListener('mouseover', overPixel);
            pixel.addEventListener('mouseout', outPixel);
            row.appendChild(pixel);
        }
        canvasElem.appendChild(row);
    }
}

let currentlyClicked = false;
document.addEventListener('mouseup', upPixel);
function upPixel(event) {
    currentlyClicked = false;
    console.log('up', event.target.id);
}

function downPixel(event) {
    currentlyClicked = true;
    console.log('down', event.target.id);
}

function outPixel(event) {
    if( currentlyClicked ){
        event.target.style.background = currentlyColor;
        console.log('out', event.target.id);
    }
}

function overPixel(event) {
    if( currentlyClicked ){
        event.target.style.background = currentlyColor;
        console.log('over', event.target.id);
    }
}
createCanvas();