/**
 * Definition of OutputCollector:
 * class OutputCollector<K, V> {
 *     public void collect(K key, V value);
 *         // Adds a key/value pair to the output buffer
 * }
 * Definition of Document:
 * class Document {
 *     public int id;
 *     public String content;
 * }
 */

class Pair {
    String key;
    int value;

    Pair(String key, int value) {
        this.key = key;
        this.value = value;
    }
}

public class TopKFrequentWords {

    public static class Map {
        public void map(String _, Document value,
                        OutputCollector<String, Integer> output) {
            // Output the results into output buffer.
            // Ps. output.collect(String key, int value);

            for (String word : value.content.split(" ")) {
                if (word.length() > 0) {
                    output.collect(word, 1);
                }
            }
        }
    }


    public static class Reduce {
        private PriorityQueue<Pair> queue;
        private int k;

        private Comparator<Pair> pairComparator = new Comparator<Pair>() {
            public int compare(Pair left, Pair right) {
                if (left.value != right.value) {
                    return left.value - right.value;
                }
                return right.key.compareTo(left.key);
            }
        };

        public void setup(int k) {
            this.k = k;
            queue = new PriorityQueue<Pair>(k, pairComparator);
        }

        public void reduce(String key, Iterator<Integer> values) {
            // sum up
            int sum = 0;
            while (values.hasNext()) {
                sum += values.next();
            }
            Pair pair = new Pair(key, sum);

            // compare
            if (queue.size() < k) {
                queue.add(pair);
            } else {
                Pair top = queue.peek();
                if (pairComparator.compare(pair, top) > 0) {
                    queue.poll();
                    queue.add(pair);
                }
            }
        }

        public void cleanup(OutputCollector<String, Integer> output) {
            // Output the top k pairs <word, times> into output buffer.
            // Ps. output.collect(String key, Integer value);

            List<Pair> pairs = new ArrayList<Pair>(queue);
            while (!queue.isEmpty()) {
                pairs.add(queue.poll());
            }

            // reverse result
            for (int i = pairs.size() - 1; i >= 0; --i) {
                Pair pair = pairs.get(i);
                output.collect(pair.key, pair.value);
            }
        }
    }
}