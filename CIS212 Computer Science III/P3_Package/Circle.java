package P3_Package;

import java.lang.Math;

public class Circle implements AreaMeasurable{
	private double _radius;
	
	public Circle(double r){
		_radius = r;
	}
	
	@Override
	public double getArea(){
		return Math.PI * Math.pow(_radius, 2);
	}
	
}
