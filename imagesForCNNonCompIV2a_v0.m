clc
clear all
close all
currentdirectory = pwd;
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
subID=1; %Enter the name of the Participant
session='T';
taskName='Left';
bandName='Mu';



if(strcmp(taskName,'Left')==1)
    task=1; %Enter the classlabel of the task:= 1:Right, 2:Left: Here the patient was right impaired
elseif(strcmp(taskName,'Right')==1)
    task=2;  
elseif(strcmp(taskName,'Feet')==1)
    task=3; 
elseif(strcmp(taskName,'Tongue')==1)
    task=4; 
end
 
 %Enter Frequency band Mu[8 12]/Beta[16 24]; 
if(strcmp(bandName,'Mu')==1)
    band=[8 12]; %Enter the classlabel of the task:= 1:Right, 2:Left: Here the patient was right impaired
elseif(strcmp(bandName,'Beta')==1)
    band=[16 24];  
end

MovingWin=250; %smoothing window for ERD calculation
order=4;
fs=250; %sampling frequency
[B_u,A_u]=butter(order,band/fs*2); 

activityPeriod=[3.5 4.5];
baseLinePeriod=[1 2]; %Enter the desired baseline period before cue
load([currentdirectory '\Data_Parsed\parsed_A0' num2str(subID) session '.mat']);
% load(['Data_Parsed\parsed_A0' num2str(subID) session '.mat']);

   
taskLabels=find(cleanClassLabels==task);
taskSpecificTrials=cleanRawEEGData(taskLabels,:,:);

for trl=1:size(taskSpecificTrials,1)
    for ch=1:size(taskSpecificTrials,2)
        temp=squeeze(taskSpecificTrials(trl,ch,:));
        tempFilt=filter(B_u,A_u,temp);
        tempFilt=tempFilt';
        tempFiltPwSm = smooth(tempFilt.^2,MovingWin);
        erd(trl,ch)=mean(tempFiltPwSm(round(activityPeriod(1)*fs):round(activityPeriod(2)*fs)))/mean(tempFiltPwSm(round(baseLinePeriod(1)*fs):round(baseLinePeriod(2)*fs)));
    end
end

pot=ones(1,81);

if(strcmp(session,'T')==1)
    sub3='Train';
else
    sub3='eval';
end

srcOut=[currentdirectory '\FeaturesIm\A0' num2str(subID) '\' sub3 '\'];

for trl=1:size(erd,1)

%     pot(17)=erd(trl,1);
%     pot(26:30)=[erd(trl,2:6)];
%     pot(36:42)=[erd(trl,7:13)];
%     pot(48:52)=[erd(trl,14:18)];
%     pot(60:62)=[erd(trl,19:21)];
%     pot(70)=erd(trl,22);
    
    pot(17)=1;
    pot(26:30)=ones(1,5);
    pot(36:42)=[1 erd(trl,8) 1 1 1 erd(trl,12) 1];
    pot(48:52)=ones(1,5);
    pot(60:62)=ones(1,3);
    pot(70)=1;

    topoplot(pot,'Standard-10-20-Cap81.locs','headrad',0.46,'conv','on','shading','interp','mapLimits',[0 2]);
%     saveas(gcf,[srcOut 'A0' num2str(subID) '_' session '_'  bandName '_tr' num2str(trl) '_' num2str(activityPeriod(1)) 's_' num2str(activityPeriod(2)) 's_' taskName '.png']);
    set(gcf,'PaperUnits','inches','PaperPosition',[0 0 3 2.5]);
%     print -dpng temp.png -r100
%     imshow('temp.png');

    saveas(gcf,[srcOut 'A0' num2str(subID) '_' session '_'  bandName '_tr' num2str(trl) '_' num2str(activityPeriod(1)) 's_' num2str(activityPeriod(2)) 's_' taskName '.png']);
    
    close all
end


