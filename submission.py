YELLOW = color(255, 255, 0)

ORANGE = color(255, 133, 51)

RED = color(200, 0, 0)

DARK_BROWN = color(40, 20, 10)

CENTER_RED = color(255, 128, 128)

YELLOW1 = color(255, 204, 0)

YELLOW2 = color(255, 255, 128)

YELLOW3 = color(255, 255, 153)

WHITE = color(255, 255, 255)

LCORAL = color(255, 199, 179)

DARK_RED = color(153, 0, 51)

PINK = color(255, 0, 102)

VIOLET = color(153, 0, 153)

LIGHT_VIOLET = color(255, 0, 255)

LIGHT_ORANGE = color(255, 136, 77)

GREEN = color(51, 204, 51)

DCYAN = color(0, 153, 153)

LCYAN = color(51, 204, 204)

LLCYAN = color(173, 235, 235)

MAJ = color(153, 51, 102)

MAJ2 = color(204, 102, 153)

MAJ3 = color(236, 198, 215)

CORAL = color(255, 162, 128)

ellipse1 = ellipse(w=110, h=100, fill=MAJ) | translate(x=140)

ellipse2 = ellipse(w=95, h=86, fill=MAJ2) | translate(x=135)

ellipse3 = ellipse(w=80, h=72, fill=MAJ3) | translate(x=130)

petal_unit = ellipse1 + ellipse2 + ellipse3

diamond_unit = (

    rectangle(w=60, h=60, fill=YELLOW) +

    rectangle(w=45, h=45, fill=LIGHT_ORANGE) +

    rectangle(w=30, h=30, fill=WHITE)

) | rotate(45)

petal_ring = petal_unit | repeat(12, rotate(30))

star = diamond_unit | translate(x=40) | repeat(8, rotate(45)) | scale(1.1)

fringe_unit = rectangle(w=30, h=5, fill=DARK_RED)

fringe = fringe_unit | translate(x=178) | repeat(36, rotate(10))

center_petal1 = ellipse(w=80, h=30, fill=VIOLET)

center_petal2 = ellipse(w=70, h=26, fill=LIGHT_VIOLET)

center_petal3 = ellipse(w=60, h=22, fill=PINK)

center_petal_unit = center_petal1 + center_petal2 + center_petal3

center_flower = center_petal_unit | translate(x=30) | repeat(10, rotate(36))

shape1 = rectangle(w=250, h=250, fill=DARK_RED) | repeat(8, rotate(11.25))

shape2 = rectangle(w=220, h=220, fill=ORANGE) | rotate(5.6) | repeat(8, rotate(11.25))

shape3 = rectangle(w=205, h=205, fill=ORANGE) | rotate(5.6) | repeat(8, rotate(11.25))

shape4 = rectangle(w=190, h=190, fill=YELLOW1) | repeat(8, rotate(11.25))

shape5 = rectangle(w=175, h=175, fill=YELLOW3) | rotate(5.6) | repeat(8, rotate(11.25))

shape6 = rectangle(w=130, h=130, fill=YELLOW) | repeat(8, rotate(11.25))

center_star_point = rectangle(w=15, h=1.5, fill=WHITE)

center_star_design = center_star_point | repeat(6, rotate(60))

shapePP = rectangle(w=60, h=5, fill=WHITE) | rotate(10) | repeat(10, rotate(30))

dopetal = circle(r=5, fill=RED) | translate(x=20)

doring = dopetal | repeat(12, rotate(30))

new_ring_petal = circle(r=5, fill=GREEN)

new_ring = new_ring_petal | translate(x=95) | repeat(33, rotate(11.25))

pookalam = (

    circle(r=220, fill=DARK_RED) +

    circle(r=200, fill=ORANGE) +

    circle(r=190, fill=YELLOW1) +

    shape1 +

    shape2 +

    petal_ring +

    shape3 +

    shape4 +

    shape5 +

    circle(r=110, fill=RED) +

    new_ring +

    circle(r=80, fill=WHITE) +

    circle(r=70, fill=WHITE) +

    shape6 +

    circle(r=80, fill=CORAL) +

    circle(r=70, fill=LCORAL) +

    center_flower +

    circle(r=20, fill=LIGHT_ORANGE) +

    center_star_design

) | scale(0.6)

show(pookalam)
