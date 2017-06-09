/* *****************************************************************************
 * A.L.E (Arcade Learning Environment)
 * Copyright (c) 2009-2013 by Yavar Naddaf, Joel Veness, Marc G. Bellemare,
 *  Matthew Hausknecht, and the Reinforcement Learning and Artificial Intelligence 
 *  Laboratory
 * Released under the GNU General Public License; see License.txt for details. 
 *
 * Based on: Stella  --  "An Atari 2600 VCS Emulator"
 * Copyright (c) 1995-2007 by Bradford W. Mott and the Stella team
 *
 * *****************************************************************************
 *  sharedLibraryInterfaceExample.cpp 
 *
 *  Sample code for running an agent with the shared library interface. 
 **************************************************************************** */

#include <iostream>
#include <ale_interface.hpp>

#ifdef __USE_SDL
  #include <SDL.h>
#endif

using namespace std;

ALEInterface ale1;

class Checkspeed
{
public:
int color,started,numframes;
std::string status;

};

class Rows
{
public:
int color,calculated,threat,numframes,started,numframes1,startc,endc,length,startp,endp,covered,numactions;
float speed;
std::string direction;
int actions[3];

};

Rows rows[195];
Checkspeed sp[195];

int calcrow(int y,int frame)
{
ALEScreen screen=ale1.getScreen();
int startp=0,endp=0;
float fsp1=0,fep1=0;



if((y<102 && rows[y].direction=="right") || (y>=104 && rows[y].direction=="left"))
{
printf("row-%d",y);
exit(0);
}





	for(int j=9;j<screen.width();j++)
	{	
	if(screen.get(y,j)==rows[y].startc)
	{
		startp=j;
		break;
	}
	}
	for(int j=screen.width()-1;j>8;j--)
	{
	if(screen.get(y,j)==rows[y].endc)
	{
		endp=j;
		break;
	}
	}





if(y==180 || y==178)
{
printf("row-%d-startco-%d-endco-%d-start-%d-end-%d\n",y,rows[y].startc,rows[y].endc,startp,endp);
if(startp==0 && endp==0 && y==180)
{

	for(int j=9;j<screen.width();j++)
	{	
	if(screen.get(y,j)==0)
	{
		startp=j;
		break;
	}
	}
	for(int j=screen.width()-1;j>8;j--)
	{
	if(screen.get(y,j)==0)
	{
		endp=j;
		break;
	}
	}

}
}






	if(rows[y].direction=="right")
	{
		int dist=ceil(rows[y].speed*frame);
		float dist1=(float)rows[y].speed*(float)frame;
		if(startp==9 || endp==(screen.width()-1))
		{
			
			
			if(endp==(screen.width()-1))
			{
				endp=startp+rows[y].length-1;
				endp=endp+dist;
				startp=endp-rows[y].length+1;
				if(startp<=screen.width())
				{
				endp=8;
				startp=endp-rows[y].length+1;
				}
				else
				{
					endp=8+(startp%screen.width());
					startp=endp-rows[y].length+1;
				}	
			}
			else if(startp==9)
			{
				endp=endp+dist;
				startp=endp-rows[y].length+1;
				if(endp>=screen.width())
				{
					if(startp<=screen.width())
					{
					endp=8;
					startp=endp-rows[y].length+1;
					}
					else
					{
						endp=8+(startp%screen.width());
						startp=endp-rows[y].length+1;
					}						
				}
							
			}

		}
		else if(startp>9 && startp<screen.width() && endp>9 && endp<(screen.width()-1))
		{
			endp=endp+dist;
			startp=endp-rows[y].length+1;
			if(endp>screen.width()-1)
			{
					if(startp<=screen.width())
					{
					endp=8;
					startp=endp-rows[y].length+1;
					}
					else
					{
						endp=8+(startp%screen.width());
						startp=endp-rows[y].length+1;
					}
			}
		}

		fsp1=startp;
		fep1=(endp+dist1-dist+1);
		
	}
	else if(rows[y].direction=="left")
	{
		int dist=ceil(rows[y].speed*frame);
		float dist1=(float)rows[y].speed*(float)frame;
		if(startp==9 || endp==(screen.width()-1))
		{
			if(startp==9)
			{

				
				endp=endp-dist;
				startp=endp-rows[y].length+1;
				if(endp>=8)
				{
				startp=0;
				}
				else
				{
					startp=screen.width()-(8-endp);
					endp=startp+rows[y].length-1;
				}	

			}
			else if(endp==(screen.width()-1))
			{
				startp=startp-dist;
				endp=startp+rows[y].length-1;
				if(endp<8)
				{
					startp=screen.width()-(8-endp);
					endp=startp+rows[y].length-1;
				}
			}
		}
		else if(startp>9 && startp<screen.width() && endp>9 && endp<(screen.width()-1))
		{
			startp=startp-dist;
			endp=startp+rows[y].length-1;
			if(startp<8)
			{
				if(endp<8)
				{
					startp=screen.width()-(8-endp);
					endp=startp+rows[y].length-1;
				}
			}
			
		}
		fsp1=startp;
		fep1=(endp-dist1+dist+1);
	}

if(y==180 || y==178)
{
printf("row-%d-frame-%d-speed-%f-start-%f-end-%f\n",y,frame,rows[y].speed,fsp1,fep1);
}


if((fsp1>44 && fsp1 <50) || (fep1>44 && fep1<50))
{
printf("startflo%f-endfloat-%f\n",fsp1,fep1);
return y; 

}
else
return 0;
}

int calcthreat(int miny,int topoint)
{
int threatpoint=0;

	for(int i=1;i<miny-topoint-1;i++)
	{
		if(miny-i-topoint<7)
		{	
			for(int j=miny-i;j>topoint;j--)
			{
				
				if(rows[j].threat==1)
				if(rows[j].calculated==1)
				{
					threatpoint=calcrow(j,i);
				}
				if(threatpoint!=0)
				break;
			}
		}
		else
		{
			for(int j=miny-i;j>miny-i-7;j--)
			{
				
				if(rows[j].threat==1)
				if(rows[j].calculated==1)
				{
					threatpoint=calcrow(j,i);
				}
				if(threatpoint!=0)
				break;
			}
		}
		
		if(threatpoint!=0)
		break;
	}
return threatpoint;
}



Action knaction(int miny,int maxy)
{


ActionVect legal_actions = ale1.getMinimalActionSet();
int topoint=0,threatpoint=0,ty=0;

	if(rows[miny].covered==0)
	{
		if(rows[miny].numactions==0)
		{
		rows[miny].numactions=1;
		return legal_actions[2];
		}
		else if(rows[miny].numactions==1)
		{
		rows[miny].numactions=2;
		return legal_actions[0];
		}
		else if(rows[miny].numactions==2)
		{
		rows[miny].numactions=3;
		rows[miny].covered=1;
		return legal_actions[1];
		}
	}
	else if(rows[miny].covered==1)
	{
		for(int i=miny-1;i>0;i--)
		{
			if(rows[i].covered==0)
			{
			topoint=i;
			break;
			}
		}
	}
	
	
	threatpoint=calcthreat(miny,topoint);
	if(threatpoint==0)
	return legal_actions[1];
	else
	return legal_actions[0]; 
}





void getminmaxy(int* miny,int* maxy)
{
*miny=1;
*maxy=1;



ALEScreen screen= ale1.getScreen();
		*miny=screen.height();
		
		*maxy=0;
		
            
		for(int i=0;i<195;i++)
		for(int j=9;j<screen.width()/2;j++)
		{
			if(screen.get(i,j)==30)
			{
				if(*miny>i)
				*miny=i;
				
				if(*maxy<i)
				*maxy=i;
				
			}

		}

		if(*maxy>=108 && *maxy<=111)
		*miny=*maxy-6;
		if(*maxy>111)
		{
			*miny=screen.height();
			for(int i=105;i<195;i++)
			for(int j=9;j<screen.width()/2;j++)
			{       if(screen.get(i,j)==30)
				if(*miny>i)
				*miny=i;
			}
		}
		
		if(*miny<=98 && *miny>=95)
		*maxy=*miny+6;
		if(*miny<95)
		{
			*maxy=0;
			for(int i=0;i<102;i++)
			for(int j=9;j<screen.width()/2;j++)
			{       if(screen.get(i,j)==30)
				if(*maxy<i)
				*maxy=i;
			}
		}
		




}



void updatespeed(int miny,int maxy)
{


ALEScreen screen=ale1.getScreen();


int u=0;
int v=0;



for(int i=0;i<195;i++)
{

	if(rows[i].numframes1>60 && rows[i].direction=="none")
	{	
		rows[i].threat=0;
		
	}
}


for(int i=miny;i<=maxy;i++)
{
for(int j=45;j<=49;j++)
{
	if(screen.get(i,j)!=191 && screen.get(i,j)!=14 && screen.get(i,j)!=157 && screen.get(i,j)!=169 && screen.get(i,j)!=30 &&  screen.get(i,j)!=238 && i<185 && i>23)
	{
		u=0;
		v=0;
		if(rows[i].threat==0)
			{
			
				rows[i].color=screen.get(i,j);
				rows[i].started=0;
				rows[i].calculated=0;
				
				rows[i].threat=1;
				printf("%d\n",i);
				rows[i].speed=0;
				rows[i].numframes1=0;
				rows[i].numframes=0;
				rows[i].length=0;
				rows[i].direction="none";
				
			}

	}
}
}




for(int i=0;i<=194;i++)
{
	if(rows[i].threat==1)
	{
		if(rows[i].calculated==0)
		{
			if(rows[i].started==0)
			{
				
				if(rows[i].direction=="right")
				{
					
					if(screen.get(i,9)==rows[i].endc)
					{
					rows[i].started=1;
					rows[i].numframes=0;
					}
				}
				else if(rows[i].direction=="left")
				{
					
					if(screen.get(i,screen.width()-1)==rows[i].startc)
					{
					rows[i].started=1;
					rows[i].numframes=0;
					}
				}
			}
			else if(rows[i].started==1)
			{
				if(rows[i].direction=="right")
				{
					if(screen.get(i,screen.width()-1)==rows[i].endc)
					{
					
						rows[i].speed=(float)((float)screen.width()/(float)rows[i].numframes);
					
						rows[i].calculated=1;
						if(i== 180 || i==178)
						printf("180- spedd-%f",rows[i].speed);
					}
					else
					rows[i].numframes++;
				}
				else if(rows[i].direction=="left")
				{
					if(screen.get(i,9)==rows[i].startc)
					{
						
						rows[i].speed=(float)((float)screen.width()/(float)rows[i].numframes);
						

						rows[i].calculated=1;						
					}
					else
					rows[i].numframes++;
				}
			}


			if(rows[i].direction=="none")
			{
				
				if(rows[i].numframes1==50)
				{
					for(int j=9;j<screen.width();j++)
					{
						if(screen.get(i,j)!=191 && screen.get(i,j)!=14 && screen.get(i,j)!=157 && screen.get(i,j)!=169 && 									screen.get(i,j)!=30 &&  screen.get(i,j)!=238 && i<185 && i>23)
						{
							rows[i].startc=screen.get(i,j);
							rows[i].startp=j;
							
							break;
						}
					}

					for(int j=screen.width()-1;j>8;j--)
					{
						if(screen.get(i,j)!=191 && screen.get(i,j)!=14 && screen.get(i,j)!=157 && screen.get(i,j)!=169 && 									screen.get(i,j)!=30 &&  screen.get(i,j)!=238 && i<185 && i>23)
						{
							rows[i].endc=screen.get(i,j);
							rows[i].endp=j;
							break;
						}
					}
					rows[i].length=rows[i].endp-rows[i].startp+1;

					
				}
				
				if(rows[i].numframes1==60)
				{
					int disp=0;
					for(int j=9;j<screen.width();j++)
					{	
						
						if(screen.get(i,j)==rows[i].startc)
						{
							disp=rows[i].startp-j;	
							
							break;
						}
					}
					if(disp<0)
					{
					rows[i].direction="right";
					//cout<<"row-"<<i<<"-"<<rows[i].direction<<endl;
					}					
					else if(disp>0)
					{
					rows[i].direction="left";
					//cout<<"row-"<<i<<"-"<<rows[i].direction<<endl;					
					}
				}	
				rows[i].numframes1++;
			}

		}

	}
}



}




int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "Usage: " << argv[0] << " rom_file" << std::endl;
        return 1;
    }



for(int i=0;i<195;i++)
{
//sp[i].status="unknown";
rows[i].threat=0;
rows[i].covered=0;
rows[i].numactions=0;

}

    

    // Get & Set the desired settings
    ale1.setInt("random_seed", 123);
    //The default is already 0.25, this is just an example
    ale1.setFloat("repeat_action_probability", 0.25);

#ifdef __USE_SDL
    ale1.setBool("display_screen", true);
    ale1.setBool("sound", true);
#endif
	int z=0;
    // Load the ROM file. (Also resets the system for new settings to
    // take effect.)
    ale1.loadROM(argv[1]);

    // Get the vector of legal actions
    ActionVect legal_actions = ale1.getMinimalActionSet();
	int maxy=0,miny=0;
    // Play 10 episodes
    for (int episode=0; episode<10; episode++) {

		for(int i=0;i<195;i++)
		{
		//sp[i].status="unknown";
		if(rows[i].threat==1)
		if(rows[i].calculated==0)
		rows[i].threat=0;

		}
		
        float totalReward = 0;
        while (!ale1.game_over()) {
            Action a = legal_actions[1];
		
            // Apply the action and get the resulting reward
		if(z>10)
		{		
		getminmaxy(&miny,&maxy);

		updatespeed(miny,maxy);

		}

		
		
		
            float reward = ale1.act(knaction(miny,maxy));
            totalReward += reward;
	z++;
        }
        cout << "Episode " << episode << " ended with score: " << totalReward << endl;
        ale1.reset_game();
    }

    return 0;
}
