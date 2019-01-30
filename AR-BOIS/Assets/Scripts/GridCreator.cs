using System;
using System.IO;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GridCreator : MonoBehaviour
{  
    public Transform [] buildingMassive;

    public List <string> readedLines;
    ArrayList buildings = new ArrayList();

    int bias, cntPair;
   
    public struct Paths{ 
      public int x; 
      public int y; 
    } 
    
    public struct Building
    { 
      public string name; 
      public int xAxis; 
      public int yAxis;
    }

    public Transform [] markers;
    public Transform quad;
    
     
    int[] path; 
    Vector3[] pathWay;
    Vector3 time, temp;
    float quadHeight = 1f;
    float quadWidth = 1f;
    const float eps = 0.2f;
    
    public float GridHeight;
    public float GridWidth;
    
    float x;
    float y;
    
    float Ratio_X;
    float Ratio_Y;

    bool needToChangeScale = false;
    void Start()
    {
        FindCoordinates();
        LoadTXT();
        Ratio_X = x/(GridWidth*2);
        Ratio_Y = y/(GridHeight*2);
        CreateGrid();
    }
    void Update()
    {
       FindNewScale();
       if(needToChangeScale)
       {
           ChangeScale();
       }
    }

    void FindCoordinates()
    {
       x = Math.Abs(markers[0].position.x - markers[1].position.x);
       y = Math.Abs(markers[0].position.z - markers[1].position.z);
    }
    
    void CreateGrid()
    {
       for(int i = 0; i < GridWidth; i++)
       {
           for(int j = 0; j < GridHeight; j++)
           {
               Transform cell = Instantiate(quad) as Transform;
               time = cell.localScale;
               time.x *= Ratio_X;
               time.z *= Ratio_Y;
               cell.localScale = time;

               cell.position = markers[0].position + new Vector3(i*2*time.x, 0f, j*2*time.z) + time;
               cell.parent = this.transform;
               cell.name = i + " " + j;
           }
       }
       CreateBuildings();
    }
    
    void FindNewScale()
    {
        if (Math.Abs(x - Math.Abs(markers[0].position.x - markers[1].position.x)) > eps || Math.Abs(y - Math.Abs(markers[0].position.z - markers[1].position.z)) > eps)
        {
            Ratio_X = Math.Abs(markers[0].position.x - markers[1].position.x)/(GridWidth*2);
            Ratio_Y = Math.Abs(markers[0].position.z - markers[1].position.z)/(GridHeight*2);
            needToChangeScale = true;
        }
    }

    public void LoadTXT() 
    { 
        int counter = 0;
        
        string subLine;
        string sepLine; 
        

        StreamReader theReader = new StreamReader("/Users/romanfedorov/AR-BOIS/Assets/Scripts/output.txt");

        using(theReader)
        {
            while(true)
            {
                subLine = theReader.ReadLine();
                if(subLine != null)
                {
                    readedLines.Add(subLine);
                }
                else 
                {
                    theReader.Close();
                    break;
                }
            }
        }
        
        GridWidth = float.Parse(readedLines[0].Split(' ')[0]); 
        GridHeight = float.Parse(readedLines[0].Split(' ')[1]);
        bias = Convert.ToInt32(readedLines[0].Split(' ')[2]); 
        
        for(int i = 1; i < bias + 1; i++)
        { 
            sepLine = readedLines[i]; 
            Building buildingNEW = new Building();
            buildingNEW.name = sepLine.Split(' ')[0]; 
            buildingNEW.xAxis = Convert.ToInt32(sepLine.Split(' ')[1]); 
            buildingNEW.yAxis = Convert.ToInt32(sepLine.Split(' ')[2]); 
            buildings.Add(buildingNEW);
        } 
    }
     void CreateBuildings()
        {
            foreach(Transform build in buildingMassive)
            {
                foreach(Building ToBuild in buildings)
                {
                    if(build.gameObject.tag == ToBuild.name)
                    {
                        Transform BUILDING = Instantiate(build) as Transform;
                        foreach(Transform guy in transform)
                        {
                            if(guy.name == ToBuild.xAxis + " " + ToBuild.yAxis)
                               BUILDING.position = guy.position;
                        }
                        if(BUILDING.gameObject.tag == "church")
                        {
                            BUILDING.localScale = time/2;
                        }
                        else if(BUILDING.gameObject.tag == "theater") 
                        {
                            BUILDING.localScale = time/4;
                        }
                        else if(BUILDING.gameObject.tag == "university")
                        {
                            BUILDING.localScale = time/15;
                        }
                        else if(BUILDING.gameObject.tag == "burgers")
                        {
                            BUILDING.localScale = time/7;
                        }
                        else 
                            BUILDING.localScale = time/5;
                        BUILDING.parent = this.transform;
                    }
                }
            }
        }
          
        void ChangeScale()
        {
            needToChangeScale = false;
            foreach (Transform grd in transform)
            {
                Destroy(grd.gameObject);
            }
            CreateGrid();
        }
    }
