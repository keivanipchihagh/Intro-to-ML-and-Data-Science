package com.company;

import java.util.Random;

/**
 * <h1>DNA object storing genes which define a unique (as we call) phrase</h1>
 * <p>
 * A class to describe a pseudo-DNA, i.e. genotype
 * Here, a virtual organism's DNA is an array of character.
 * Functionality:
 * -- convert DNA into a string
 * -- calculate DNA's "fitness"
 * -- mate DNA with another set of DNA
 * -- mutate DNA
 * </p>
 * @author Keivan Ipchi Hagh
 * @version 1.0.3
 * @since 2019
 */
public class DNA {

    /**
     * An array to hold characters
     */
    private char[] genes;

    /**
     * Fitness score of the current DNA
     */
    private float fitness;

    /**
     * java.util.Random
     */
    Random random = new Random();

    /**
     * DNA Constructor
     * @param target Target string
     */
    public DNA(String target) {
        genes = new char[target.length()];
        for (int i = 0; i < genes.length; i++)
            genes[i] = (char)(random.nextInt(96) + 32);     // Select a random character in bounds of 32, 128
    }

    /**
     * Calculate the overall fitness of the current DNA as percentage
     * @param target Target string
     */
    public void calculateFitness(String target) {
        int score = 0;
        for (int i = 0; i < genes.length; i++)
            if (genes[i] == target.charAt(i))
                score++;
        fitness = (float)score / genes.length;  // Percentage format
        this.fitness = (float)Math.pow(fitness, 2);    // Exp value
    }

    /**
     * Crossover algorithm; Select a random middle point and inherit from parents accordingly
     * @param partner Other parent DNA
     * @param target Target string
     * @return Child DNA
     */
    public DNA crossover(DNA partner, String target) {

        DNA child = new DNA(target);
        int midPoint = random.nextInt(genes.length);    // A random index from the length

        for (int i = 0; i < genes.length; i++)
            if (i < midPoint)
                child.genes[i] = genes[i];
            else
                child.genes[i] = partner.genes[i];

        return child;
    }

    /**
     * Mutate DNA to keep variety in the population
     * @param mutationRate Mutation Rate
     */
    public void mutate(float mutationRate) {

        for (int i = 0; i < genes.length; i++)
            if (Math.random() < mutationRate)
                genes[i] = (char)(random.nextInt(96) + 32);
    }

    /**
     * Convert character array to string
     * @return string of genes
     */
    public String getPhrase() {
        return new String(genes);
    }

    /**
     * Getter: Get fitness
     * @return DNA's Fitness
     */
    public float getFitness() { return fitness; }
}
