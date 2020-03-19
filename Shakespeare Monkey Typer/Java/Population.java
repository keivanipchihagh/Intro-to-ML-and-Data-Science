package com.company;

import java.util.ArrayList;
import java.util.Random;

/**
 * <h1>Population ecosystem</h1>
 *
 * <p>
 * A class to describe a population of virtual organisms
 * In this case, each organism is just an instance of a DNA object
 * </p>
 *
 * @author Keivan Ipchi Hagh
 * @version 1.0.3
 * @since 2019
 */
public class Population {

    /**
     * Indicates mutation rate for each child DNA
     */
    float mutationRate;
    /**
     * Total DNA population array
     */
    DNA[] population;
    /**
     * Mutation pool ArrayList for natural selection
     */
    ArrayList<DNA> matingPool;
    /**
     * Target string
     */
    String target;
    /**
     * Current generation index
     */
    int generations;
    /**
     * Search status
     */
    boolean finished;
    /**
     * Best fitness score
     */
    int perfectScore;
    /**
     * java.util.Random
     */
    Random random = new Random();

    /**
     * Population Constructor
     *
     * @param target          Target string
     * @param mutationRate    Mutation rate
     * @param populationCount Populatin count
     */
    public Population(String target, float mutationRate, int populationCount) {
        this.target = target;
        this.mutationRate = mutationRate;
        population = new DNA[populationCount];

        // Initialize each DNA
        for (int i = 0; i < populationCount; i++)
            population[i] = new DNA(target);

        calculateFitness();
        matingPool = new ArrayList<>();
        finished = false;
        generations = 0;
        perfectScore = 1;
    }

    /**
     * Calculate fitness for each DNA
     */
    public void calculateFitness() {
        for (int i = 0; i < population.length; i++)
            population[i].calculateFitness(target);
    }

    /**
     * Perform natural selection using NOC algorithm
     */
    public void naturalSelection() {
        matingPool.clear();

        // Find best fitness score
        float maxFitness = 0;
        for (int i = 0; i < population.length; i++)
            if (population[i].getFitness() > maxFitness)
                maxFitness = population[i].getFitness();

        for (int i = 0; i < population.length; i++) {

            int DNACount = (int) (population[i].getFitness() * 100);
            for (int j = 0; j < DNACount; j++)
                matingPool.add(population[i]);  // Add selected DNA to mating pool for further process
        }
    }

    /**
     * Generate a new generation and inherit properties from parents to children.
     * Also, replace children with parents to minimize memory usage
     */
    public void generate() {

        for (int i = 0; i < population.length; i++) {

            // Select two random parent DNAs
            DNA parent1 = matingPool.get(random.nextInt((matingPool.size())));
            DNA parent2 = matingPool.get(random.nextInt((matingPool.size())));

            DNA child = parent1.crossover(parent2, target);   // Generate new child
            child.mutate(mutationRate);  // Mutate child
            population[i] = child;  // Replace with old generation DNA
        }
        generations++;
    }

    /**
     * Get average fitness score
     *
     * @return Average fitness score
     */
    public float getAverageFitness() {
        float total = 0;
        for (int i = 0; i < population.length; i++)
            total += population[i].getFitness();

        return total / (population.length);
    }

    /**
     * Is search finished?
     *
     * @return boolean indicating whether search for newer generation has ended or not.
     */
    public boolean isFinished() {
        return finished;
    }

    /**
     * Get generation
     *
     * @return new generation
     */
    public int getGenerations() {
        return generations;
    }

    /**
     * Gets best phrase; If fitness score is '1', then we found the phrase
     * @return Best phrase
     */
    public String getBestPhrase() {

        float worldrecord = 0;
        int index = 0;

        // Search for the best fitness score
        for (int i = 0; i < population.length; i++)
            if (population[i].getFitness() > worldrecord) {
                index = i;
                worldrecord = population[i].getFitness();
            }

        // If best score is found, then stop the search
        if (worldrecord == perfectScore)
            finished = true;

        return population[index].getPhrase();
    }
}
