package P3_Package;

public class Rectangle implements AreaMeasurable{
	double _length;
	double _width;
	
	public Rectangle(double l, double w){
		_length = l;
		_width = w;
	}
	
	@Override 
	public double getArea(){
		return _length * _width;
	}
}
