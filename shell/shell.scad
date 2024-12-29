// Parameters for the hemisphere
radius = 25;  // Radius of the hemisphere

module hemisphere(radius) {
    difference() {
        // Full sphere
        sphere(r = radius, $fn = 100);

        // Remove the lower half
        translate([0, 0, -radius/2])
            cube([radius * 2, radius * 2, radius], center = true);
    }
}

difference() {
    hemisphere(radius);
    hemisphere(radius-1);
    rotate([57, 0, 0]) {
         cylinder(radius*2, 2.5, 2.5);
    }
}