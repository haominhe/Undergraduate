"""
Agenda display for MeetMe and MeetMeAgain projects. 
Author:  Michal Young, for CIS 210, July 2014.

Display one or more agendas in columns for a given
period in a single day (skipping appointments on different
days or outside the display period). 
"""

from graphics import *    # Zelle's simple OO graphics
from agenda import Agenda, Appt
import datetime

def time_diff_seconds(begin, end):
    """
    Calculate the difference between begin and end,
    to the nearest second. 
    Args: 
         begin: a datetime.time object
         end:  a datetime.time object, which should be after begin
    Return: 
         floor of number of seconds from begin to end
    Notes:  Although datetime provides a timedelta type, it provides 
        arithmetic on datetime and date objects, but not on time objects. 
        Thus we roll our own substitute for subtracting times, independent
        of date. 
    """
    dummy_day = datetime.date(2000, 1, 1)
    begin_dt = datetime.datetime.combine(dummy_day, begin)
    end_dt = datetime.datetime.combine(dummy_day, end)
    diff = end_dt - begin_dt
    return diff.seconds


class Display():
    """
    A graphical display of appointments within a given time period in a given time.
    Multiple agendas can be displayed in different columns.
    """

    def __init__(self, width, height, date, min_time, max_time , n_cols ):
        """Create the agenda display.
        Args: 
           width:  Width of display in pixels
           height: Height of display in pixels
           min_time:  Earliest time displayable in window, as datetime.time object
           max_time:  Latest time displayable in window, as datetime.time object
           n_cols:  Window is divided into this many columns for agendas or days

           Note because of margins, standard coordinate transforms get tricky.
           We're going to work in native dimensions. 
        """

        self.win = GraphWin("Agenda", width, height)
        self.win.setCoords(0, 0, width, height)  # Pixel units
        bkgrnd = Rectangle( Point(0,0), Point(width,height) )
        bkgrnd.setFill( color_rgb(230,230,230) ) # Grey background
        bkgrnd.draw(self.win)

        self.left_margin = 20  # too thin?
        self.col_width = (width - self.left_margin)/n_cols
        self.header_height = 20
        self.bottom_margin = 5
        self.col_height = height - (self.bottom_margin + self.header_height)
        self.date = date 
        self.earliest_time = min_time
        self.latest_time = max_time
        self.schedule_span_seconds = time_diff_seconds(min_time, max_time)

        ## Hour labels on left
        label_time = datetime.time(hour=0, minute=0)
        for label_hour in range(24):
            label_time = label_time.replace(hour = label_hour)
            if label_time >= min_time and label_time <= max_time:
                # print("Labeling hour ", label_time)
                xcenter = self.left_margin / 2 
                ycenter = self.time_to_y(label_time)
                label = Text( Point(xcenter, ycenter), str(label_hour))
                label.setFace("helvetica")
                label.setSize(10)
                label.setFill( color_rgb(0,0,0))
                label.draw(self.win)

        self.cur_col = 0
        self.appt_color = color_rgb(255,255,255)  # Default is white

    @classmethod
    def from_appt(cls, appt, n_cols, width=700, height=500):
        """
        Factory creates a display based on an appointment.
        Args:
           appt:  Take the date, begin, and end from this Appt object
           n_cols: Number of columns for agendas
           width, height: pixel dimensions of display
        Returns:
           a Display object
        """
        date = appt.begin.date()
        start = appt.begin.time()
        end = appt.end.time()
        return Display(width, height, date, start, end, n_cols)


    def time_to_y(self, time):
        """Translate time of day to y coordinate in window.
        Args:
           time:  a datetime.time between the min and max time set in the 'make' call
        Returns:
           a y coordinate proportionally scaled to the schedule area of the window,
           growing downward from top of schedule column
        """
        time_as_seconds = time_diff_seconds(self.earliest_time, time)
        proportion =  time_as_seconds / self.schedule_span_seconds
        ycoord =  self.bottom_margin  + self.col_height * (1 - proportion)
        return ycoord

    def set_color(self, red, green, blue):
        """
        Subsequent appointments should be shaded an rgb shade(red, green, blue)
        Args:
           red: integer 0..255 indicating red component of RGB color
           blue: integer 0..255 indicating red component of RGB color
           green: integer 0..255 indicating blue component of RGB color
        Examples disp.set_color(0,0,0) sets appointment color to black,
           disp.set_color(250,250,250) sets them to light grey, and
           disp.set_color(250,0,250) sets them to a purple shade.
        self.appt_color = color_rgb(255,255,255)  # Default is white
        """
        self.appt_color = color_rgb(red, green, blue)  

    def next_column(self):
        self.cur_col += 1

    def label_column(self, text):
        """Display the text at the top of the current column"""
        ycenter = self.bottom_margin + self.col_height + 0.5 * self.header_height
        xcenter = self.left_margin + (self.cur_col + 0.5) * self.col_width
        label = Text( Point(xcenter,ycenter), text)
        label.setFace("helvetica")
        label.setSize(10)
        label.setFill( color_rgb(0,0,0) )
        label.draw(self.win)


    def display_appt(self, appt):
        """
        Display an appointment in the current column.
        Args:
           appt:  An Appt object
        """
        from_time = max(appt.begin.time(), self.earliest_time)
        to_time = min(appt.end.time(), self.latest_time)
        if from_time >= to_time:
            print("Appt off display area: ", appt)  #DEBUG
            return
        lly = self.time_to_y(to_time)
        ury = self.time_to_y(from_time)
        llx = self.left_margin + self.cur_col*self.col_width
        urx = llx + self.col_width
        appt_rect = Rectangle(Point(llx, lly), Point(urx, ury))
        appt_rect.setFill(self.appt_color)
        appt_rect.draw(self.win)
        xcenter = (llx + urx) / 2
        ycenter = (lly + ury) / 2
        label = Text( Point(xcenter, ycenter), appt.desc)
        label.setFace("helvetica")
        label.setSize(10)
        label.setFill( color_rgb(0,0,0))
        label.draw(self.win)

    def display_agenda(self, agenda):
        """
        Display the appointments of an agenda on a particular date
        in the current column.  Appointments on other days are ignored.
        Args:
           agenda: an Agenda object
           date: a datetime.date object.  Only appointments on this date are displayed.
        """
        for appt in agenda:
            if appt.begin.date() == self.date:
                print("DISPLAYING: " + str(appt))
                self.display_appt(appt)

if __name__ == "__main__":
    print("This is just a quick test of the display")
    display = Display(700,500,  datetime.date(2014,3,14), 
                      datetime.time( hour=7),
                      datetime.time(hour=19), 3)
    appt = Appt( datetime.date(2014,3,14),
                 datetime.time(8,00),
                 datetime.time(15,00),
                 "Sample 8-3")
    display.display_appt(appt)
    display.label_column("Mary")
    display.next_column()
    display.label_column("Ted")
    appt = Appt( datetime.date(2014,3,14),
                 datetime.time(9,0),
                 datetime.time(11),
          "Sample 9-11")
    display.display_appt(appt)
    display.next_column()

    ag = Agenda()
    ag.append(Appt.from_string("2014.9.30 9:00 10:30 | Brush teeth"))
    ag.append(Appt.from_string("2014.9.30 12:00 14:30 | Get on bus"))
    ag.append(Appt.from_string("2014.3.14 5:00 9:00 | Up early"))
    ag.append(Appt.from_string("2014.3.14 14:00 18:00 | Afternoon"))
    ag.append(Appt.from_string("2014.3.14 16:00 17:00 | Overlapping"))
    ag.append(Appt.from_string("2014.3.14 20:00 23:00 | After hours"))
    display.set_color(100,255,100) # Greenish?
    display.display_agenda(ag)
    

    input("Press enter to close")
    
