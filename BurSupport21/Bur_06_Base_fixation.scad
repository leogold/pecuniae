
difference() { //fixation hole
    translate ([0,0,3]) cylinder (d=15, h=6, $fs=0.1, center=true);
    difference() { //chamfer
        translate ([0,0,4]) cylinder (d=5.4, h=7, $fs=0.1, center=true);
        translate ([1.7,-3.5,0]) cube([7,7,7]);
        translate ([-8.7,-3.5,0]) cube([7,7,7]);   
    }
}


difference() {

translate ([0,0,-2.5]) cylinder (d=30, h=5.2, $fs=0.1, center=true);

    translate ([0,0,-3.5]) cylinder (d1=25, d2=20, h=4, $fs=0.1, center=true);
    translate ([0,0,-4.1]) cylinder (d=2.1, h=15, $fs=0.1, center=true);
}
