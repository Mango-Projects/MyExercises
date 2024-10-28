import java.io.File;
import java.util.Scanner;

class Bag {
	String receiptdate;
	int freight;
	int unitcost;

	Bag(String $receiptdate, int $unitcost) {
		receiptdate = $receiptdate;
		unitcost = $unitcost;
	}
}

class Air extends Bag {
	int deliveryhours;
	Air(String $receiptdate, int $unitcost, int $deliveryhours) {
		super($receiptdate, $unitcost);
		deliveryhours = $deliveryhours;
	}
	double computeFreight() {
		return unitcost * deliveryhours;
	}
}

public class JPA06 {
	public static void main(String args[]) {
		try {
			Scanner scanner = new Scanner(System.in);
			int unitcost = scanner.nextInt();
			scanner.close();
			if (!(unitcost >= 0)) {
				System.out.print("error");
				return;
			}

        	String pathname = "read.txt";
			File file = new File(pathname);
			Scanner reader = new Scanner(file);
			
			double totalDeliveryhours = 0;
			for (int i = 0; i < 5; i++) {
				String[] data = reader.nextLine().split(",");
				Air air = new Air(data[0], unitcost, Integer.parseInt(data[1]));
				totalDeliveryhours += air.computeFreight();
			}
			reader.close();
			System.out.print((int)totalDeliveryhours);
		} catch (Exception e) {
			System.out.print("error");
			return;
		}
	}
}
