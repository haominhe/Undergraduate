package P4_Package;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Main {
	private static PaintPanel _paintPanel;
	
	public static void main(String[] args) {
		JFrame mainFrame = new JFrame("Main");
		mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		mainFrame.setLayout(new BorderLayout());
		
		_paintPanel = new PaintPanel();
		mainFrame.add(_paintPanel, BorderLayout.CENTER);
		
		JButton BlackBtn = new JButton("Black");
		BlackBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				_paintPanel.colorBlack();
			}
		});
		
		
		JButton GreenBtn = new JButton("Green");
		GreenBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				_paintPanel.colorGreen();
			}
		});
		
		
		JButton YellowBtn = new JButton("Yellow");
		YellowBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				_paintPanel.colorYellow();
			}
		});
		
		
		JButton GrayBtn = new JButton("Gray");
		GrayBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				_paintPanel.colorGray();
			}
		});
		
		
		JButton SmallBtn = new JButton("Small");
		SmallBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				_paintPanel.sizeSmall();
			}
		});
		
		
		JButton MediumBtn = new JButton("Medium");
		MediumBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				_paintPanel.sizeMedium();
			}
		});
		
		
		JButton LargeBtn = new JButton("Large");
		LargeBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				_paintPanel.sizeLarge();
			}
		});
		
		
		JButton ClearBtn = new JButton("Clear");
		ClearBtn.addActionListener(new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent ev) {
				_paintPanel.clearButton();
			}
		});
		
		
		
		JPanel colorPanel = new JPanel();
		colorPanel.setLayout(new GridLayout(4,1));
		colorPanel.add(BlackBtn); colorPanel.add(GreenBtn); 
		colorPanel.add(YellowBtn); colorPanel.add(GrayBtn);
		
		
		JPanel sizePanel = new JPanel();
		sizePanel.setLayout(new GridLayout(4,1));
		sizePanel.add(SmallBtn); sizePanel.add(MediumBtn);
		sizePanel.add(LargeBtn); sizePanel.add(ClearBtn);
		
		
		mainFrame.add(colorPanel, BorderLayout.WEST);
		mainFrame.add(sizePanel, BorderLayout.EAST);
		mainFrame.setVisible(true);
		mainFrame.pack();
	}

}

















