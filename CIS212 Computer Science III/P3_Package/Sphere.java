package P3_Package;

import java.lang.Math;

public class Sphere implements AreaMeasurable{
	private double _radius;
	
	public Sphere(double r){
		_radius = r;
	}
	
	@Override
	public double getArea(){
		return 4 * Math.PI * Math.pow(_radius, 2);
	}
}
