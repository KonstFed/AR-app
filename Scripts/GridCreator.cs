using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GridCreator : MonoBehaviour
{  
    public float GridHeight;
    public float GridWidth;
    
    float quadHeight;
    float quadWidth;
    public Transform [] markers;
    float x;
    float y;
    float new_oldx;
    float new_oldy;
    public width;
    public heigth;
    public BuildingMap[] buildings;
    public int[] path;
    int counter = 0;
    const eps = 0.5;
    public Paths[] pathWay;
    void Start()
    {
        
    }
    struct Paths{
        public x;
        public y;
    }
    struct BuildingMap{
        public name;
        public xAxis;
        public yAxis;

    }
    public void LoadTXT() {

                string[] readedLines = File.ReadAllLines(".txt"); 
                int lineCounter = -1;
                string sepLine;
                GridWidth = readedLines[0].split(" ")[0];
                GridHeight = readedLines[0].split(" ")[1];
                int bias = readedLines[0].split(" ")[2]
                for(int i = 1; i<bias + 1; i++) {
                    sepLine = readedLines[i];
                    BuildingMap[i-1].name = sepLine.split(" ")[0];
                    BuildingMap[i-1].xAxis = sepLine.split(" ")[1];
                    BuildingMap[i-1].yAxis = sepLine.split(" ")[2];
                }
                int cntPair = readedLines[bias+1];
                int[] mas = readedLines[bias+2].split(" ");

                for (int j = 0; j < cntPair;j= j + 2){
                    pathWay[j/2].x  = mas[j];
                    pathWay[j/2].y = mas[j+1];
                }
                //LoadCells(); //Вызов события загрузки блоков
        }
    void Update()
    {
        if (Abs(x - markers[0].position.x - markers[1].position.x )> eps or Abs(y - markers[0].position.y - markers[1].position.y)>eps){
            new_oldx = markers[0].position.x - markers[1].position.x/x;
            new_oldy = markers[0].position.y - markers[1].position.y/y;
            //Марк запили тут для скэйла для моделек
            x = x * new_oldx;
            y = y * new_oldy;

        }
    }

    void FindCoordinates()
    {
    
       x =Abs(markers[0].position.x - markers[1].position.x);
       y =Abs(markers[0].position.y - markers[1].position.y);
       quadWidth = x/GridWidth;
       quadHeight = y/quadHeight;
    }
    void CreateGrid()
    {
       
    }
}
