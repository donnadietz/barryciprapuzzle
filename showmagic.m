#define squarenumber as some integer between 1 and 7040

function []  = showmagic(squarenumber,M,tiles)

holdsquare=M(squarenumber,1:16);
h=holdsquare;


imshow([tiles(125*h(1)+1:125*h(1)+125, 1:125),tiles(125*h(2)+1:125*h(2)+125, 1:125),tiles(125*h(3)+1:125*h(3)+125, 1:125),tiles(125*h(4)+1:125*h(4)+125, 1:125);
	tiles(125*h(5)+1:125*h(5)+125, 1:125),tiles(125*h(6)+1:125*h(6)+125, 1:125),tiles(125*h(7)+1:125*h(7)+125, 1:125),tiles(125*h(8)+1:125*h(8)+125, 1:125);
        tiles(125*h(9)+1:125*h(9)+125, 1:125),tiles(125*h(10)+1:125*h(10)+125, 1:125),tiles(125*h(11)+1:125*h(11)+125, 1:125),tiles(125*h(12)+1:125*h(12)+125, 1:125);
	tiles(125*h(13)+1:125*h(13)+125, 1:125),tiles(125*h(14)+1:125*h(14)+125, 1:125),tiles(125*h(15)+1:125*h(15)+125, 1:125),tiles(125*h(16)+1:125*h(16)+125, 1:125)]);    
title(squarenumber);


