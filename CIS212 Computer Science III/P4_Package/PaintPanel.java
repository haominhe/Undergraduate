package P4_Package;

/* CIS 212    Spring 2015     Assignment 4 GUI
 * Haomin He 
 * To gain exposure to Java Swing and to build a user interface with a mix of standard and 
 * custom widgets. To create a simple interactive paint application. 
 */

import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.ArrayList;


public class PaintPanel extends JPanel {
	/* Add a canvas to the window which draws points when the user clicks the canvas or
	 * drags the mouse on the canvas. The number of points that can appear on the screen 
	 * simultaneously should be unbounded. Create a class to hold the data of current 
	 * point color, size and the coordinates for each point.
	 * 
	 * Add at least 3 buttons to window which will allow the user to select the current
	 * point size. This point size should affect any points drawn from the time the size 
	 * is selected until the time that another size is selected. 
	 */
	private static final int SMALL_POINT_SIZE = 10;
	private static final int MEDIUM_POINT_SIZE = 25;
	private static final int LARGE_POINT_SIZE = 40;
	
	private ArrayList<PaintPoint> old_pointsAL;
	private ArrayList<Point> _pointsAL;
	private Color _color;
	private int _size;
	
	public PaintPanel() {
		setPreferredSize(new Dimension(630, 630));
		setBackground(Color.WHITE);
		
		old_pointsAL = new ArrayList<PaintPoint>();
		_pointsAL = new ArrayList<Point>();
		_color = Color.BLACK;
		_size = MEDIUM_POINT_SIZE;
		
		MousePaintAdapter mpa = new MousePaintAdapter();
		addMouseMotionListener(mpa);
	}
	
	
	private class PaintPoint {
		// This class will records the old points that the user has dragged over
		private final ArrayList<Point> dragged_old_points;
		private final Color old_color;
		private final int old_size;
		
		public PaintPoint(ArrayList<Point> oldpoints, Color oldcolor, int oldsize) {
			dragged_old_points = oldpoints;
			old_color = oldcolor;
			old_size = oldsize;
		}
		public ArrayList<Point> getoldpoints() { return dragged_old_points; }
		public Color getoldcolor() { return old_color; }
		public int getoldsize() { return old_size; }
	}
	
	
	private class MousePaintAdapter extends MouseAdapter {
		@Override
		public void mouseDragged(MouseEvent ev) {
			_pointsAL.add(ev.getPoint());
			repaint();
			// get the current position on to the current point list, then repaint
		}
	}
	
	
	@Override
	public void paintComponent(Graphics graphics) {
		super.paintComponent(graphics);
		// print the old points, then print the new points
		for (PaintPoint oldpts : old_pointsAL) {
			graphics.setColor(oldpts.getoldcolor());
			int oldsz = oldpts.getoldsize();
			for (Point point : oldpts.getoldpoints()) {
				graphics.fillOval(point.x, point.y, oldsz, oldsz);
			}
		}
		graphics.setColor(_color);
		for (Point newpts : _pointsAL) {
			graphics.fillOval(newpts.x, newpts.y, _size, _size);
		}
	}
	
	
	/* Add at lease four buttons to the window which allow the user to select the
	 * current point color. This point color should affect any points drawn from 
	 * the time the color is selected until the time that another color is selected.
	 * 
	 * Store the previous color first, then change the color to the new color.
	 */
	public void colorBlack(){
		if (_color != Color.BLACK) {
			old_pointsAL.add(new PaintPoint(_pointsAL, _color, _size));
			_pointsAL = new ArrayList<Point>();
			repaint();
			_color = Color.BLACK;
		}
	}
	
	
	public void colorGreen(){
		if (_color != Color.GREEN) {
			old_pointsAL.add(new PaintPoint(_pointsAL, _color, _size));
			_pointsAL = new ArrayList<Point>();
			repaint();
			_color = Color.GREEN;
		}
	}
	
	
	public void colorYellow(){
		if (_color != Color.YELLOW) {
			old_pointsAL.add(new PaintPoint(_pointsAL, _color, _size));
			_pointsAL = new ArrayList<Point>();
			repaint();
			_color = Color.YELLOW;
		}
	}
	
	
	public void colorGray(){
		if (_color != Color.GRAY) {
			old_pointsAL.add(new PaintPoint(_pointsAL, _color, _size));
			_pointsAL = new ArrayList<Point>();
			repaint();
			_color = Color.GRAY;
		}
	}
	
	
	/* Add at least 3 buttons to the window which will allow the user to select the
	 * current point size. This point size should affect any points drawn from 
	 * the time the size is selected until the time that another size is selected.
	 * 
	 * Store the previous size first, then change the size to the new size.
	 */
	public void sizeSmall(){
		if (_size != SMALL_POINT_SIZE) {
			old_pointsAL.add(new PaintPoint(_pointsAL, _color, _size));
			_pointsAL = new ArrayList<Point>();
			repaint();
			_size = SMALL_POINT_SIZE;
		}
	}
	
	
	public void sizeMedium(){
		if (_size != MEDIUM_POINT_SIZE) {
			old_pointsAL.add(new PaintPoint(_pointsAL, _color, _size));
			_pointsAL = new ArrayList<Point>();
			repaint();
			_size = MEDIUM_POINT_SIZE;
		}
	}
	
	
	public void sizeLarge(){
		if (_size != LARGE_POINT_SIZE) {
			old_pointsAL.add(new PaintPoint(_pointsAL, _color, _size));
			_pointsAL = new ArrayList<Point>();
			repaint();
			_size = LARGE_POINT_SIZE;
		}
	}
	
	
	
	/* Add a clear button to the frame which, when clicked, immediately clears anything 
	 * that has been drawn to the canvas. 
	 */
	public void clearButton() {
		old_pointsAL = new ArrayList<PaintPoint>();
		_pointsAL = new ArrayList<Point>();
		repaint();
	}

}






















