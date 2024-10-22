clc
clear all
close all
%%%BCI Competition Dataset-IV_2a 
%%Number of Subjects=9, Number of Sessions=2, Number of Runs in each
%%Session=6 with 48 trials, total=48x6=288 trials in each session. The time
%%in a trial=6s, cue appears at 2s for 1.25s. SamplingRate=250Hz. Total EEG
%%channels used =22,
%%%         Fz(17),
%%% FC3(26),FC1(27),FCz(28),FC2(29),FC4(30),
%%%C5(36),C3(37),C1(38),Cz(39),C2(40),C4(41),C6(42),
%%% CP3(48),CP1(49),CPz(50),CP2(51),CP4(52),
%%%      P1(60),Pz(61),P2(62),
%%%         POz(70)


%%
subID=7; %Enter the name of the Participant
session='T';
taskName='L';
bandName='M';
cue=2;

if(taskName=='L')
    task=1; %Enter the classlabel of the task:= 1:Right, 2:Left: Here the patient was right impaired
elseif(taskName=='R')
    task=2;  
elseif(taskName=='F')
    task=3; 
elseif(taskName=='T')
    task=4; 
end

 %Cue given at 2s in a trial of 0 to 6s.
 
if(bandName=='M')
    band=[8 12]; %Enter the classlabel of the task:= 1:Right, 2:Left: Here the patient was right impaired
elseif(taskName=='B')
    band=[16 24];  
end

 %Enter Frequency band Mu[8 12]/Beta[16 24];
  

MovingWin=250; %smoothing window for ERD calculation
order=4;
fs=250; %sampling frequency
[B_u,A_u]=butter(order,band/fs*2); 

act=0.5; %starting time point for activity period
baseLinePeriod=[-1 0]+cue; %Enter the desired baseline period before cue
load(['Data_Parsed/parsed_A0' num2str(subID) session '.mat']);

   
taskLabels=find(cleanClassLabels==task);
taskSpecificTrials=cleanRawEEGData(taskLabels,:,:);

inst=0;
hop=0.25;
win=0.5;
stTime=2.5;
trlLength=6;

for trl=1:size(taskSpecificTrials,1)
   for tmSeg=stTime:hop:trlLength-win
        inst=inst+1;
        activityPeriod=[tmSeg tmSeg+win];
            for ch=1:size(taskSpecificTrials,2)
                temp=squeeze(taskSpecificTrials(trl,ch,:));
                tempFilt=filter(B_u,A_u,temp);
                tempFilt=tempFilt';
                tempFiltPwSm = smooth(tempFilt.^2,MovingWin);
                erd(inst,ch)=mean(tempFiltPwSm(round(activityPeriod(1)*fs):round(activityPeriod(2)*fs)))/mean(tempFiltPwSm(round(baseLinePeriod(1)*fs):round(baseLinePeriod(2)*fs)));
            end
            
    end
end

pot=ones(1,81);

for trl=1:size(erd,1)

    pot(17)=erd(trl,1);
    pot(26:30)=[erd(trl,2:6)];
    pot(36:42)=[erd(trl,7:13)];
    pot(48:52)=[erd(trl,14:18)];
    pot(60:62)=[erd(trl,19:21)];
    pot(70)=erd(trl,22);

    % topoplot(pot,'Standard-10-20-Cap81.locs','electrodes','labels','headrad',0.46,'conv','on','shading','interp','mapLimits',[0 2]);
    topoplot(pot,'Standard-10-20-Cap81.locs','headrad',0.46,'conv','on','shading','interp','mapLimits',[0 2]);
    saveas(gcf,['imgA0' num2str(subID) '_' session '_'  bandName '_' taskName '_' num2str(trl) '.png']);
    pause;
    close all
end


