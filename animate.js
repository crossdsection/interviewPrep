function sunRaft() {
$("#sun").animate({ opacity: .7 }, 1000).animate({ opacity: 1 }, 1000);
$("#raft").animate({ top: '-=5px' }, 1000).animate({ top: '+=5px' }, 1000);
$("#raftripple").animate({ opacity: .1 }, 1000).animate({ opacity: 1 }, 1000);
setTimeout(sunRaft, 2000);
}

function cloud1() {
$("#cloud1").animate({ left: '+=850px' }, 10000).animate({ left: '-150px' }, 0);
setTimeout(cloud1, 10000);
}

function cloud2() {
$("#cloud2").animate({ left: '+=950px' }, 9000).animate({ left:"-250px" }, 0);
setTimeout(cloud2, 9000);
}

function cloud3() {
$("#cloud3").animate({ left: '+=800px' }, 6000).animate({ left: '-100px' }, 0);
setTimeout(cloud3, 6000);
}

function animation() {
    sunRaft();
    cloud1();
    cloud2();
    cloud3();
}

setTimeout(animation, 300);

  