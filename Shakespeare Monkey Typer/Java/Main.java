package com.company;

public class Main {

    final static String target = "to be or not to be";
    final static float mutationRate = (float)0.09;
    final static int  populationCount = 1000;

    public static void main(String[] args) {

        Population population = new Population(target, mutationRate, populationCount);

        while (true) {
            population.naturalSelection();
            population.generate();
            population.calculateFitness();

            System.out.println(population.getBestPhrase() + " - " + population.generations + " - " + population.getAverageFitness());

            // Break if search is done.
            if (population.isFinished())
                break;
        }

    }
}
