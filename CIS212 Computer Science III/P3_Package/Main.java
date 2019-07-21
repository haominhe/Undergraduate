package P3_Package;

import java.util.Random;
import java.lang.Double;
import java.util.ArrayList;

public class Main {
		private static double nextRandomNonzeroDouble(){
			Random random = new Random();
			double numDouble = random.nextDouble();
			//Math.random() is [0, 1) and Double.MIN_VALUE is the smallest
			//possible positive value, Math.random() + Double.MIN_VALUE is (0, 1]
			//The largest number Math.random() will return is the largest possible 
			//double-precision floating point number less than 1.0, 
			//which is 1.0 - Double.MIN_VALUE.
			return numDouble + Double.MIN_VALUE;
		}
		
		private static double calculateSum(ArrayList<AreaMeasurable> shapes){
			double areasum = 0.0;
			if (shapes.size() != 0) {
				for (AreaMeasurable each : shapes){
					areasum += each.getArea();
				}
			}
			return areasum;
		}
			
		public static void main(String[] args) {
			// Populates that list with 1000 random instances of AreaMeasurable classes.
			// Each AreaMeasurable should be created with random dimensions using the
			// nextRandomNonzeroDouble() method.
			
			Random randomshape = new Random();			
			ArrayList<AreaMeasurable> listshapes = new ArrayList<AreaMeasurable>();			
			int circles = 0, ractangles = 0, squares = 0, spheres = 0, boxes = 0, cubes = 0;
			// Track the number of instances of each class created and print the results.
			
			for (int i = 0; i < 1000; ++i){
				int currshape = randomshape.nextInt(6);
				if (currshape == 0){
					++circles;
					listshapes.add(new Circle(nextRandomNonzeroDouble()));
				} else if (currshape == 1){
					++ractangles;
					listshapes.add(new Rectangle(nextRandomNonzeroDouble(), nextRandomNonzeroDouble()));
				} else if (currshape == 2){
					++squares;
					listshapes.add(new Square(nextRandomNonzeroDouble(), nextRandomNonzeroDouble()));
				} else if (currshape == 3){
					++spheres;
					listshapes.add(new Sphere(nextRandomNonzeroDouble()));
				} else if (currshape == 4){
					++boxes;
					listshapes.add(new Box(nextRandomNonzeroDouble(), nextRandomNonzeroDouble(), nextRandomNonzeroDouble()));
				}else if (currshape == 5){
					++cubes;
					listshapes.add(new Cube(nextRandomNonzeroDouble(), nextRandomNonzeroDouble(), nextRandomNonzeroDouble()));
				}	
			} 
			double sumareas = calculateSum(listshapes);
			
			System.out.printf("circles: %d rects: %d squares: %d spheres: %d boxes: %d cubes:%d\n", 
							   circles, ractangles, squares, spheres, boxes, cubes);
			System.out.println("sum: " + sumareas);
			
	}

}
