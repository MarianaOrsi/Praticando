package com.aulasdepoo.aula17.codigosPG;

public class CodigoPGMainThrowsException {
    public static void main(String[] args) {
        try {
            CodigoPGExemplosThrowsException1 data = new CodigoPGExemplosThrowsException1(0,10,2000);
        } catch (Exception e) {
            e.printStackTrace(); // captura o erro lançado na exception
        }
    }
}
