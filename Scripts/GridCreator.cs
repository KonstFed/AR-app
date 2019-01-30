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

    public BuildingMap[] buildings;
    public int[] path;
    
    const eps = 0.5;
    public Paths[] pathWay;
    void Start()
    {
        
    }
    struct Paths{
        public int x;
        public int y;
    }
    struct BuildingMap{
        public string name;
        public int xAxis;
        public int yAxis;

    }
    public void LoadTXT() {
        string sepLine;
        string[] readedLines = File.ReadAllLines("output.txt"); 
        GridWidth = Convert.ToInt(readedLines[0].split(" ")[0]);
        GridHeight = Convert.ToInt(readedLines[0].split(" ")[1]);
        int bias = Convert.ToInt(readedLines[0].split(" ")[2]);
        for(int i = 1; i<bias + 1; i++) {
            sepLine = readedLines[i];
            buildings[i-1].name = sepLine.split(" ")[0];
            buildings[i-1].xAxis = Convert.ToInt(sepLine.split(" ")[1]);
            buildings[i-1].yAxis = Convert.ToInt(sepLine.split(" ")[2]);
        }
        int cntPair = readedLines[bias+1];
        string[] mas = readedLines[bias+2].split(" ");
        int counter = 0;
        foreach (string p in mas)
        {
            if(counter % 2 == 0){
               pathWay[counter/2].x  = Convert.ToInt(p);
            }
            else {
               pathWay[counter/2].y = Convert.ToInt(p);
            }
            counter++;
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
