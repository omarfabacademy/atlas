pr=10;               //Pipeline Raduis
ph=20;              //pipeline Height
sr=10;               //Sensor Raduis
lr=20;               //Liquid Raduis
sn=4;               //Number of Sensors
sh=20;              // Sensor Height
ch=10;              //Circuit Height
cr=30;               //Circle Raduis
margin=sr*4;      //Distance between sensors and the Cube
x0=0;               //Origin for X
y0=0;               //Origin for Y
z0=0;               //Origin for Z
sl=4*sr;            //Distance Between Sensors

xc=x0+(sl*(sn+1))+(2*sr*sn)+(2*margin);               //Cube X Dim
yc=y0+(sr*2*4)+(cr*20);                                                 //Cube Y Dim
zc=z0+(sh*5)+(2*ch);                                            //Cube Z  Dim
xs=x0+margin+sl+sr;               //Sensors Positios x
ys=y0+(yc/2);               //Sensors Positios y
zs=z0+zc-sh;               //Sensors Positios z

thickness=5;               //Thickness of the 
difference(){
union(){
difference() {
difference() {
    translate([x0,y0,z0]) 
    cube([xc,yc,zc]);
    translate([x0+thickness,y0+thickness,z0+thickness]) 
    cube([xc-(thickness*2),yc-(thickness*2),zc-(thickness*2)]);
     echo("omar");  

    
}

for(i=[0:1:sn-1])
    {
    translate([xs+(i*(sl+2*sr)),ys,zs])
    cylinder(h=sh, r1=sr , r2=sr, center=false); 
      echo(i);  
    }
    translate([xc/2,2*sr,zc/2])
rotate([90,0,0])
cylinder(h=ph, r1=pr , r2=pr, center=false); 
    rotate([0,0,0])

translate ([xc/2,yc/2,0])
cylinder(h=sl, r1=lr , r2=lr, center=false); 
 
    
}

translate ([xc/2,yc/2,0])
difference (){
sphere(r = cr+2);
sphere(r=cr);
rotate([180,0,0])    
cylinder(h=cr+2, r1=cr+2 , r2=cr+2, center=false); 
    

}




}









}