package com.company;

import static java.lang.Math.pow;

public class Main {

    final static String target = "to be or not to be";
    final static float mutationRate = (float)0.01;
    final static int  populationCount = 100;

    public static void main(String[] args) {

        Population population = new Population(target, mutationRate, populationCount);

        while (true) {
            population.naturalSelection();
            population.generate();
            population.calculateFitness();

            System.out.println(population.getBestPhrase() + " - " + population.generations + " - " + population.getAverageFitness());

            // Break if search is done.
            if (population.isFinished()) {
                System.out.println("Search took " + System.currentTimeMillis() / pow(10, 12) + " seconds to complete.");
                break;
            }
        }

    }
}
