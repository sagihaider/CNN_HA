%%%TrialCutter%%%%
%%%This program cuts all the trials from BCI competition IV 2a dataset and
%%%stacks them in the following format: trialIndex X Samples in a trial
%%%(which is a 2D matrix). Additionally there would be an information about
%%%the labels in a 1d array
clc
clear all
close all
session='T';
trlLength=6;
eegChannels=1:22;
tic
for subID=3:3
    [s, HDR] = sload(['A0' num2str(subID) session '.gdf']);
  
    nOfTrials=length(HDR.TRIG);
    trlStartIndexes=HDR.TRIG;
    sampRate=HDR.SampleRate;
    

    for trl=1:nOfTrials
        for ch=1:size(s,2)
            rawData(trl,ch,:)=s(trlStartIndexes(trl):trlStartIndexes(trl)+(trlLength*sampRate)-1,ch);
        end
    end

    goodTrials=find(HDR.ArtifactSelection==0);
    cleanRawData=rawData(goodTrials,:,:);
    cleanRawEEGData=cleanRawData(:,eegChannels,:);

    classLabels=HDR.Classlabel;
    cleanClassLabels=classLabels(goodTrials);

    eval(['save([''parsed_A0'' num2str(subID) session ''.mat''],''cleanRawEEGData'',''cleanClassLabels'')']);
   % clear s HDR rawData cleanRawData cleanRawEEGData 
    [subID toc]
end