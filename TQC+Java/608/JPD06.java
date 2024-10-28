import java.io.File;
import java.io.FileReader;
import java.io.BufferedReader;
import java.util.Scanner;

class Bag {
	String receiptdate;
	int freight;
	int unitcost;

	Bag() {
	}
}
// TO DO -class Air
public class JPD06 {
	public static void main(String args[]) {
		try {
        	String pathname = "read.txt";
			File f = new File(pathname);
			FileReader fr = new FileReader(f);
			BufferedReader br = new BufferedReader(fr);

			String line = "";
			String[] date = new String[5];
			int[] hour = new int[5];



			// TO DO




		} catch (Exception e) {
			System.out.print("error");

		}
	}
}
