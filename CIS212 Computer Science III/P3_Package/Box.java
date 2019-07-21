package P3_Package;

public class Box implements AreaMeasurable{
	private double _length;
	private double _width;
	private double _height;
	
	public Box(double l, double w, double h){
		_length = l;
		_width = w;
		_height = h;
	}
	
	@Override
	public double getArea(){
		// 2*(x*y + y*z + x*z)
		return 2 * (_length * _width + _width * _height + _length * _height);
	}
}
