import java.util.LinkedList;
import java.util.Queue;

class ProducerConsumer {
    private final int capacity;
    private final Queue<Integer> queue = new LinkedList<>();

    public ProducerConsumer(int capacity) {
        this.capacity = capacity;
    }

    public void produce() throws InterruptedException {
        int value = 0;
        while (true) {
            synchronized (this) {
                while (queue.size() == capacity) {
                    wait();  // Wait until space is available
                }

                System.out.println("Produced " + value);
                queue.add(value++);

                notify();  // Notify consumers that new data is available
                Thread.sleep(1000);
            }
        }
    }

    public void consume() throws InterruptedException {
        while (true) {
            synchronized (this) {
                while (queue.isEmpty()) {
                    wait();  // Wait until data is available
                }

                int value = queue.poll();
                System.out.println("Consumed " + value);

                notify();  // Notify producers that space is available
                Thread.sleep(1000);
            }
        }
    }

    public static void main(String[] args) {
        final ProducerConsumer pc = new ProducerConsumer(5);

        Thread producerThread = new Thread(() -> {
            try {
                pc.produce();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                e.printStackTrace();
            }
        });

        Thread consumerThread = new Thread(() -> {
            try {
                pc.consume();
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
                e.printStackTrace();
            }
        });

        producerThread.start();
        consumerThread.start();
    }
}
